# politique-graphes-open-data

=============================
Quiz Politique – Open Data
=============================

Projet réalisé dans le cadre du cours : L3 Graphes et Open Data – UFR SEGMI – Université Paris Nanterre

OBJECTIF :
----------
Ce projet a été conçu en deux parties :
1. Analyser les votes des députés à l’Assemblée nationale sur un échantillon de lois clivantes.
2. Créer un quiz interactif qui permet aux utilisateurs de voter eux-mêmes, puis de découvrir à quel groupe politique ils ressemblent le plus.

CONTENU DU DOSSIER :
---------------------
- quiz_lois.py              -> Script principal du quiz Streamlit
- votes_scrutins_final.csv -> Fichier de données (votes des députés)
- requirements.txt          -> Dépendances Python nécessaires
- README.txt                -> Ce fichier

COMMENT UTILISER LE QUIZ :
---------------------------
1. Vérifiez que vous avez Python installé sur votre ordinateur.
2. Installez les bibliothèques nécessaires (à faire une seule fois) :
    pip install -r requirements.txt

3. Lancez le quiz avec la commande suivante :
    streamlit run quiz_lois.py

Le quiz s’ouvrira automatiquement dans votre navigateur.

TECHNOS UTILISÉES :
--------------------
- Python 3
- Pandas
- BeautifulSoup (scraping HTML)
- Streamlit (interface utilisateur)
- NetworkX & Matplotlib (visualisation de graphes)

AUTEURS :
----------
Projet réalisé par deux étudiants de L3 MIAGE de l'Université de Nanterre – Avril 2025
