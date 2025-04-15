import numpy as np
import pandas as pd
import networkx as nx
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial.distance import pdist, squareform
from sklearn.preprocessing import MinMaxScaler


# 1. Chargement des données
df = pd.read_csv("deputes-active-final.csv", sep=';', encoding='utf-8-sig')
print("Colonnes disponibles :", df.columns.tolist())
print("\nAperçu des données :\n", df.head())

# 2. Nettoyage des valeurs manquantes sur les colonnes numériques
cols_numeriques = ['age', 'scoreParticipation', 'scoreLoyaute', 'scoreMajorite', 'nombreMandats']
for col in cols_numeriques:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(df[col].mean())

# 3. Création d’un identifiant unique : nom + prénom + département
df["nom_complet"] = (
    df["nom"].fillna("Inconnu").str.upper() + " " +
    df["prenom"].fillna("Inconnu").str.upper() + " (" +
    df["departementNom"].fillna("ND") + ")"
)

# 4. Sélection des variables pour l'analyse
features = df[["age", "scoreParticipation", "scoreLoyaute", "scoreMajorite", "nombreMandats"]]

# 5. Normalisation
scaler = MinMaxScaler()
features_normalized = scaler.fit_transform(features)

# 6. Calcul des distances
distance_totale = squareform(pdist(features_normalized, metric='euclidean'))
print("\nMatrice des distances (extrait) :\n", distance_totale[:5, :5])

# 7. Construction du graphe
G = nx.Graph()
for i, depute in enumerate(df["nom_complet"]):
    G.add_node(depute)
    for j in range(i + 1, len(df)):
        if distance_totale[i, j] < 0.5:  # Seuil de proximité ajustable
            G.add_edge(
                df["nom_complet"][i],
                df["nom_complet"][j],
                weight=1 - distance_totale[i, j]
            )

# 8. Clustering K-Means
n_clusters = min(3, len(df))
kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
df["groupe"] = kmeans.fit_predict(distance_totale)

# 9. Visualisation du graphe
plt.figure(figsize=(12, 8))
nx.draw(G, with_labels=True, node_color=df["groupe"], cmap=plt.cm.Set1, node_size=600, font_size=8)
plt.title("Graphe des députés basé sur l'âge, la participation, la loyauté, la majorité et les mandats")
plt.tight_layout()
plt.show()

# 10. Visualisation 2D : âge vs participation
sns.scatterplot(x=df["age"], y=df["scoreParticipation"], hue=df["groupe"], palette="Set2", s=100)
plt.xlabel("Âge")
plt.ylabel("Score de Participation")
plt.title("Clustering des députés (âge vs participation)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 11. Résumé des groupes
print("\nDéputés par groupe :")
print(df[["nom_complet", "groupe"]].sort_values(by="groupe"))


