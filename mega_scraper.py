import pandas as pd
from bs4 import BeautifulSoup

# 📁 Tous les fichiers HTML à traiter (15 lois)
fichiers = [
    "site-assemblee3213.html",  # Immigration
    "site-assemblee3945.html",  # Principes de la République
    "site-assemblee1462.html",  # Réintégration suspendus / Covid
    "site-assemblee3658.html",  # Sécurité globale
    "site-assemblee3855.html",  # Bioéthique
    "site-assemblee3891.html",  # Données personnelles
    "site-assemblee4321.html",  # Crise sanitaire
    "site-assemblee629.html",   # IVG constitution
    "site-assemblee2742.html",  # Loi Avia
    "site-assemblee997.html",   # Délimitation des régions
    "site-assemblee1120.html",  # Transition énergétique
    "site-assemblee217.html",   # Retraite juste (abro réforme)
    "site-assemblee511.html",   # Mariage pour tous
    "site-assemblee1245.html",  # Apologie du terrorisme
    "site-assemblee1191.html"   # État d’urgence post-attentats
]

votes = []

for fichier in fichiers:
    try:
        with open(fichier, encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        titre_loi = soup.title.string.strip() if soup.title else "Loi inconnue"
        print(f"🔍 Traitement : {titre_loi} ({fichier})")

        groupes = soup.find_all("ul", id=lambda x: x and x.startswith("groupe"))

        for groupe in groupes:
            h3 = groupe.find("h3")
            nom_groupe = h3.get_text(strip=True) if h3 else "Groupe inconnu"

            for section in groupe.find_all("li", class_="relative-flex"):
                titre_vote = section.find("span", class_="h6")
                type_vote = titre_vote.get_text(strip=True) if titre_vote else "Vote inconnu"

                for li in section.find_all("li", attrs={"data-acteur-id": True}):
                    nom_depute = li.get_text(strip=True)
                    votes.append({
                        "Loi": titre_loi,
                        "Groupe": nom_groupe,
                        "Député": nom_depute,
                        "Vote": type_vote
                    })

        print(f"✅ {len(votes)} votes collectés jusqu’ici.")

    except Exception as e:
        print(f"❌ Erreur avec le fichier {fichier} : {e}")

# 💾 Export final
df = pd.DataFrame(votes)
df.to_csv("votes_scrutins_final.csv", index=False, encoding="utf-8-sig")
print("📄 Fichier 'votes_scrutins_final.csv' généré avec succès avec", len(df), "lignes.")
