
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données réelles
df = pd.read_csv("deputes-active-final.csv", sep=';', encoding='utf-8-sig')

# Conversion des colonnes numériques
colonnes_numeriques = ['scoreLoyaute']
for col in colonnes_numeriques:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Calcul du score de loyauté en pourcentage
df["score_loyaute"] = df["scoreLoyaute"] * 100

# Détecter les dissidents (loyaute < 60%)
df["dissident"] = df["score_loyaute"] < 60

# Affichage des résultats
print("Députés dissidents :")
print(df[df["dissident"]][["nom", "prenom", "groupe", "score_loyaute"]])

# Visualisation du résultat
plt.figure(figsize=(14, 7))
sns.barplot(data=df, x="nom", y="score_loyaute", hue="dissident", dodge=False, palette="coolwarm")
plt.xticks(rotation=90, ha="center")
plt.xlabel("Nom du député")
plt.ylabel("Score de loyauté (%)")
plt.title("Analyse des députés fidèles vs dissidents")
plt.tight_layout()
plt.show()
