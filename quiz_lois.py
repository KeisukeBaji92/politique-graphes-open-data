import streamlit as st
import pandas as pd
from collections import Counter

st.set_page_config(page_title="📜 Quiz politique", layout="centered")

@st.cache_data
def charger_votes():
    return pd.read_csv("votes_scrutins_final.csv", encoding="utf-8-sig")

df = charger_votes()


titres_humains = {
    "Analyse du scrutin n°3213 - 16e législature - Assemblée nationale": "Contrôle de l'immigration et intégration",
    "Analyse du scrutin n°3945 - 15e législature - Assemblée nationale": "Respect des principes de la République",
    "Analyse du scrutin n°1462 - 16e législature - Assemblée nationale": "Abrogation de l’obligation vaccinale",
    "Analyse du scrutin n°3658 - 15e législature - Assemblée nationale": "Sécurité globale",
    "Analyse du scrutin n°3855 - 15e législature - Assemblée nationale": "Loi bioéthique (PMA)",
    "Analyse du scrutin n°3891 - 15e législature - Assemblée nationale": "Protection des données personnelles",
    "Analyse du scrutin n°4321 - 15e législature - Assemblée nationale": "Gestion de la crise sanitaire",
    "Analyse du scrutin n°629 - 16e législature - Assemblée nationale": "IVG dans la Constitution",
    "Analyse du scrutin n°2742 - 15e législature - Assemblée nationale": "Loi Avia (lutte contre la haine en ligne)",
    "Analyse du scrutin n°997 - 14e législature - Assemblée nationale": "Délimitation des régions",
    "Analyse du scrutin n°1120 - 14e législature - Assemblée nationale": "Transition énergétique",
    "Analyse du scrutin n°217 - 17e législature - Assemblée nationale": "Abrogation réforme des retraites",
    "Analyse du scrutin n°511 - 14e législature - Assemblée nationale": "Mariage pour tous",
    "Analyse du scrutin n°1245 - 14e législature - Assemblée nationale": "Apologie du terrorisme",
    "Analyse du scrutin n°1191 - 14e législature - Assemblée nationale": "Prolongation état d’urgence post-attentats"
}


dates = {
    "Analyse du scrutin n°3213 - 16e législature - Assemblée nationale": "19 décembre 2023",
    "Analyse du scrutin n°3945 - 15e législature - Assemblée nationale": "16 février 2021",
    "Analyse du scrutin n°1462 - 16e législature - Assemblée nationale": "4 mai 2023",
    "Analyse du scrutin n°3658 - 15e législature - Assemblée nationale": "24 novembre 2020",
    "Analyse du scrutin n°3855 - 15e législature - Assemblée nationale": "29 juin 2021",
    "Analyse du scrutin n°3891 - 15e législature - Assemblée nationale": "12 octobre 2021",
    "Analyse du scrutin n°4321 - 15e législature - Assemblée nationale": "25 juillet 2022",
    "Analyse du scrutin n°629 - 16e législature - Assemblée nationale": "30 janvier 2024",
    "Analyse du scrutin n°2742 - 15e législature - Assemblée nationale": "13 mai 2020",
    "Analyse du scrutin n°997 - 14e législature - Assemblée nationale": "25 novembre 2014",
    "Analyse du scrutin n°1120 - 14e législature - Assemblée nationale": "22 juillet 2015",
    "Analyse du scrutin n°217 - 17e législature - Assemblée nationale": "6 avril 2023",
    "Analyse du scrutin n°511 - 14e législature - Assemblée nationale": "23 avril 2013",
    "Analyse du scrutin n°1245 - 14e législature - Assemblée nationale": "5 novembre 2015",
    "Analyse du scrutin n°1191 - 14e législature - Assemblée nationale": "16 novembre 2015"
}


descriptions = {
    "loi_immigration": "Ce projet de loi vise à renforcer le contrôle de l'immigration en France, en facilitant les expulsions et en limitant l’accès à certains droits sociaux pour les étrangers en situation irrégulière. Il prévoit toutefois des mesures d'intégration, comme la régularisation de travailleurs dans des secteurs en tension. Ce texte a provoqué de fortes divisions, certains dénonçant un tournant sécuritaire, voire une reprise des idées de l’extrême droite.",
    "loi_republique": "La loi 'confortant le respect des principes de la République', surnommée loi contre les séparatismes, impose une charte de la laïcité aux associations, renforce le contrôle des écoles privées et lutte contre les discours radicaux. Portée après l’assassinat de Samuel Paty, elle a été perçue par certains comme nécessaire à l’unité nationale, mais critiquée par d’autres pour son potentiel à stigmatiser les musulmans.",
    "loi_vaccination": "Cette loi abroge l’obligation vaccinale contre la Covid-19 pour les professionnels de santé, et autorise la réintégration des soignants suspendus. Portée après l’accalmie de la pandémie, elle a ravivé les débats sur la gestion sanitaire, entre respect de la liberté individuelle et exigence de sécurité pour les patients. Certains y voient une réhabilitation, d’autres un recul en matière de santé publique.",
    "loi_securite_globale": "La loi 'Sécurité globale' vise à renforcer les pouvoirs des forces de l’ordre, autorisant notamment l’usage des drones pour surveiller les manifestations et pénalisant la diffusion malveillante d’images de policiers. Elle a été dénoncée comme une menace pour la liberté d’informer, provoquant de nombreuses mobilisations citoyennes et des critiques du Conseil des droits de l’Homme de l’ONU.",
    "loi_bioethique": "Cette loi emblématique ouvre la PMA à toutes les femmes, y compris les couples lesbiens et les femmes seules. Elle touche aussi à la recherche sur les embryons et la génétique. Saluée comme une avancée sociétale majeure pour l’égalité, elle a toutefois cristallisé les oppositions conservatrices, relançant les débats sur la filiation et les valeurs familiales traditionnelles.",
    "loi_donnees_perso": "Transposition du RGPD européen en droit français, cette loi impose de nouvelles obligations aux entreprises et aux services publics sur la gestion des données personnelles. Elle vise à mieux protéger les citoyens contre les abus numériques. Si elle fait consensus sur le fond, sa mise en œuvre a été critiquée pour sa complexité et les lourdes sanctions prévues en cas de non-respect.",
    "loi_crise_sanitaire": "Ce texte prolonge le cadre juridique de gestion des crises sanitaires, incluant le pass sanitaire, les tests obligatoires, et l’isolement de certaines personnes. Il a été vivement contesté pour son atteinte présumée aux libertés individuelles, tandis que ses partisans soulignent son efficacité face à la pandémie.",
    "loi_ivg_constitution": "Cette proposition inscrit explicitement le droit à l’IVG dans la Constitution française, en réaction à des remises en cause internationales (ex : États-Unis). Elle a été saluée comme une garantie essentielle pour les droits des femmes, mais certains y voient une instrumentalisation politique ou une mesure inutile car ce droit est déjà protégé par la loi Veil.",
    "loi_avia": "Cette loi oblige les plateformes à retirer sous 24 heures les contenus haineux signalés (racisme, antisémitisme, homophobie). Si l’intention est saluée, la loi a été partiellement censurée pour atteinte à la liberté d’expression : la suppression automatique sans décision judiciaire a suscité de vifs débats sur la censure et la modération en ligne.",
    "loi_regions": "Elle redéfinit la carte des régions françaises en passant de 22 à 13 régions métropolitaines. Présentée comme un levier d’efficacité économique, cette réforme a été vivement critiquée pour son manque de concertation, sa logique technocratique et ses effets sur l’identité régionale (ex. : la fusion Alsace-Lorraine-Champagne-Ardenne).",
    "loi_energie": "Cette loi de transition énergétique fixe des objectifs ambitieux : baisse de la consommation énergétique, réduction de la part du nucléaire, et développement des énergies renouvelables. Portée en pleine COP21, elle a suscité un fort clivage entre écologistes la jugeant trop timide et les défenseurs du nucléaire la jugeant trop risquée.",
    "loi_retraites": "Cette loi visait à annuler certaines mesures impopulaires des dernières réformes des retraites : retour à 60 ans pour certains, réduction du nombre d’annuités. Vivement soutenue par les syndicats, elle a cristallisé l’opposition entre défense d’un système solidaire et impératifs budgétaires.",
    "loi_mariage_pour_tous": "Adoptée sous la présidence de François Hollande, cette loi a ouvert le mariage aux couples de même sexe. Elle a provoqué de gigantesques mobilisations (la Manif pour tous), des débats passionnés sur la famille, la filiation, et la PMA. Un marqueur politique fort encore aujourd’hui.",
    "loi_apologie_terrorisme": "Adoptée après les attentats de 2015, cette loi renforce la pénalisation de l’apologie du terrorisme, même en ligne. Critiquée pour ses effets potentiels sur la liberté d’expression, elle a conduit à des condamnations parfois jugées excessives pour des tweets ou des propos maladroits.",
    "loi_etat_urgence": "Suite aux attentats de novembre 2015, cette loi renforce les pouvoirs de l’administration pour instaurer des perquisitions ou assignations à résidence sans juge. Votée massivement dans un contexte d’émotion nationale, elle a pourtant inquiété défenseurs des libertés et juristes, posant la question d’un glissement vers un état d’exception permanent."
}


mapping_titres = {
    k: v for k, v in zip(titres_humains.keys(), descriptions.keys())
}


mapping_urls = {
    k: f"https://www.assemblee-nationale.fr/dyn/{k.split('n°')[1].split()[1]}/scrutins/{k.split('n°')[1].split()[0]}" for k in titres_humains
}


if "index" not in st.session_state:
    st.session_state.index = 0
if "reponses" not in st.session_state:
    st.session_state.reponses = []

lois = df["Loi"].unique()


if st.session_state.index < len(lois):
    titre = lois[st.session_state.index]
    nom_humain = titres_humains.get(titre, titre)
    cle = mapping_titres.get(titre)
    description = descriptions.get(cle, "Description indisponible.")
    url = mapping_urls.get(titre)
    date = dates.get(titre)

    st.markdown(f"### 🏛️ Loi {st.session_state.index + 1} : **{nom_humain}**")
    if date:
        st.markdown(f"📅 *Adoptée le {date}*")
    st.info(description)
    if url:
        st.markdown(f"[🔗 Voir le détail du scrutin sur le site de l’Assemblée nationale]({url})")

    choix = st.radio("Quel serait votre vote ?", ["Pour", "Contre", "Abstention"], key=titre)

    if st.button("✅ Valider mon choix"):
        st.session_state.reponses.append({
            "Loi": titre,
            "Vote_utilisateur": choix
        })
        st.session_state.index += 1
        st.rerun()


else:
    st.success("🎉 Vous avez répondu à toutes les lois !")

    df_reponses = pd.DataFrame(st.session_state.reponses)
    groupes_compatibles = []

    for _, ligne in df_reponses.iterrows():
        df_filtre = df[(df["Loi"] == ligne["Loi"]) & (df["Vote"] == ligne["Vote_utilisateur"])]
        groupes = df_filtre["Groupe"].tolist()
        groupes_compatibles += groupes

    if groupes_compatibles:
        compteur = Counter(groupes_compatibles)
        meilleur_groupe, nb_votes = compteur.most_common(1)[0]
        st.markdown(f"## 🧭 Selon vos choix, vous êtes le plus proche du groupe : **{meilleur_groupe}**")
    else:
        st.markdown("🕵️ Aucun groupe politique ne ressort de vos choix.")

    for _, ligne in df_reponses.iterrows():
        df_filtre = df[(df["Loi"] == ligne["Loi"]) & (df["Vote"] == ligne["Vote_utilisateur"])]
        noms = df_filtre["Député"].tolist()

        nom_humain = titres_humains.get(ligne["Loi"], ligne["Loi"])
        st.markdown(f"---\n#### 📌 {nom_humain}")
        st.markdown(f"**Ton vote :** {ligne['Vote_utilisateur']}")
        if noms:
            st.markdown(f"**Comme :** {', '.join(noms[:10])} {'...' if len(noms) > 10 else ''}")
        else:
            st.markdown("**Aucun député n'a voté comme vous.**")

    if st.button("🔁 Recommencer le quiz"):
        st.session_state.index = 0
        st.session_state.reponses = []
        st.rerun()
