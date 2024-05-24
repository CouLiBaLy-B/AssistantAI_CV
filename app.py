# app.py
import streamlit as st
from streamlit_pills import pills
from scr.utils import extract_text_from_pdf
from scr.models import (
    ResumeImprover,
    CoverLetterGenerator,
    ScoreResumeJob,
    ResumeGenerator,
    MailCompletion,
)

st.set_page_config(page_title="Job Assistance AI", page_icon="🤖")
# Définir les styles CSS

css = """
<style>
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #4c4c4c;
    }
    .subtitle {
        font-size: 24px;
        font-weight: bold;
        color: #6c6c6c;
    }
    .description {
        font-size: 18px;
        color: #8c8c8c;
    }
</style>
"""

# Appliquer les styles CSS
st.markdown(css, unsafe_allow_html=True)

# Utiliser les styles CSS dans votre application
st.markdown("<div class='title'>Job Assistance AI</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Améliorez votre processus de candidature</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='description'>Cette application utilise des modèles d'IA pour vous aider à scorer votre CV, rédiger des lettres de motivation et améliorer votre CV.</div>",
    unsafe_allow_html=True,
)

tabMain, tabInfo, tabTo_dos = st.tabs(["Main", "Info", "To-do's"])

with tabMain:
    example = pills(
        "",
        ["CV et Offres", "Mails"],
        ["🍿", "🐎"],
        label_visibility="collapsed",
    )
    if example == "CV et Offres":
        task = st.radio(
            "Que vous voulez faire ?",
            options=(
                "Score de correspondance",
                "Rédaction de lettre de motivation",
                "Amélioration de CV",
            ),
            key="models",
        )

        resume_pdf = st.file_uploader("Import ton CV en pdf", type="pdf")

        job_advert = st.text_area("L'offre de poste",
                                  value="",
                                  height=400,
                                  key="offre")
        if resume_pdf is None:
            st.error("Veuillez importer votre CV avant de continuer.")
        elif job_advert == "":
            st.error("Veuillez saisir une description de poste avant de continuer.")
        else:
            try:
                if st.button("Lancer"):
                    with st.spinner("Wait for it..."):
                        resume = extract_text_from_pdf(resume_pdf)
                        if task == "Score de correspondance":
                            generator = ResumeGenerator(
                                resume=resume,
                                job_advert=job_advert,
                                resumeStrategy=ScoreResumeJob(),
                            )
                            generated = generator.generator()
                            st.markdown(
                                generated["text"],
                                unsafe_allow_html=True,
                            )
                        if task == "Rédaction de lettre de motivation":
                            generator = ResumeGenerator(
                                resume=resume,
                                job_advert=job_advert,
                                resumeStrategy=CoverLetterGenerator(),
                            )
                            generated = generator.generator()
                            st.write(generated["text"])
                        if task == "Amélioration de CV":
                            generator = ResumeGenerator(
                                resume=resume,
                                job_advert=job_advert,
                                resumeStrategy=ResumeImprover(),
                            )
                            generated = generator.generator()
                            st.markdown(
                                generated["text"], unsafe_allow_html=True
                            )  # st.write(generated["text"].split("Réponse :")[1])
                    st.success("Done!")
            except Exception as e:
                st.exception(f"Erreur {e}")
    if example == "Mails":
        resume_pdf = st.file_uploader(
            "Import ton CV en pdf", type="pdf", key="mail_resume"
        )
        if resume_pdf is not None:
            try:
                if st.button("Lancer", key="mail"):
                    with st.spinner("Wait for it..."):
                        resume = extract_text_from_pdf(resume_pdf)
                        generator = MailCompletion()
                        mail_complet = generator.mailcompletion(resume=resume)
                        st.write(mail_complet["text"].split("Réponse :")[1])
                    st.success("Done!")
            except Exception as e:
                st.write(f"Erreur {e}")

with tabInfo:
    st.markdown(
        "<div class='title'>À propos de cette application</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div class='description'>Cette application utilise le modèle d'IA MixTraL-8x7B-Instruct-v0.1, développé par MistralAI. Ce modèle a été entraîné sur une grande variété de tâches de traitement du langage naturel, y compris la rédaction, l'analyse et la génération de texte.</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='subtitle'>Tâches effectuées</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        "- **Score de correspondance** : Évaluer la correspondance entre votre CV et une offre d'emploi spécifique en attribuant un score sur 100 et en identifiant les points forts et les points faibles.",
        unsafe_allow_html=True,
    )
    st.markdown(
        "- **Rédaction de lettre de motivation** : Générer une lettre de motivation personnalisée en fonction de votre CV et de l'offre d'emploi.",
        unsafe_allow_html=True,
    )
    st.markdown(
        "- **Amélioration de CV** : Améliorer votre CV en intégrant les compétences, qualifications et expériences pertinentes pour l'offre d'emploi visée.",
        unsafe_allow_html=True,
    )

with tabTo_dos:
    st.markdown(
        "<div class='title'>Améliorations futures</div>", unsafe_allow_html=True
    )

    st.markdown("### Fonctionnalités supplémentaires")
    st.markdown(
        "- **Analyse des compétences** : Ajouter une fonctionnalité pour analyser les compétences du candidat à partir de son CV et fournir des recommandations pour combler les lacunes par rapport à l'offre d'emploi."
    )
    st.markdown(
        "- **Optimisation du CV pour les systèmes ATS** : Intégrer une fonctionnalité pour optimiser le CV afin qu'il soit mieux reconnu par les systèmes de suivi des candidats (ATS) utilisés par les entreprises."
    )
    st.markdown(
        "- **Suggestions de postes pertinents** : Développer une fonctionnalité pour recommander des offres d'emploi pertinentes en fonction du profil du candidat."
    )
    st.markdown(
        "- **Suivi des candidatures** : Ajouter une fonctionnalité permettant aux utilisateurs de suivre leurs candidatures et de recevoir des rappels pour les étapes suivantes."
    )

    st.markdown("### Améliorations de l'interface utilisateur")
    st.markdown(
        "- **Thème personnalisable** : Permettre aux utilisateurs de choisir un thème de couleurs personnalisé pour l'application."
    )
    st.markdown(
        "- **Mode sombre** : Ajouter un mode sombre pour une meilleure expérience dans des environnements faiblement éclairés."
    )
    st.markdown(
        "- **Aide contextuelle** : Fournir des info-bulles et des guides pour aider les utilisateurs à comprendre les différentes fonctionnalités de l'application."
    )

    st.markdown("### Intégrations supplémentaires")
    st.markdown(
        "- **Intégration avec des services d'emploi** : Permettre aux utilisateurs de se connecter à des services d'emploi populaires, comme LinkedIn ou Indeed, pour importer leurs informations de profil et postuler directement depuis l'application."
    )
    st.markdown(
        "- **Partage de CV** : Ajouter une fonctionnalité pour partager facilement le CV amélioré avec des employeurs potentiels ou des réseaux professionnels."
    )

    st.markdown("### Améliorations de performance")
    st.markdown(
        "- **Mise en cache des résultats** : Mettre en cache les résultats générés par le modèle d'IA pour accélérer les temps de réponse lors de requêtes ultérieures similaires."
    )
    st.markdown(
        "- **Traitement parallèle** : Explorer les possibilités de traitement parallèle pour accélérer les temps de réponse, en particulier pour les tâches gourmandes en ressources."
    )

    st.markdown(
        "N'hésitez pas à soumettre vos propres idées d'améliorations dans la section des commentaires ci-dessous."
    )
