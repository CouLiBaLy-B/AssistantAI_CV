```markdown
# Job Assistance AI

Job Assistance AI est une application web développée en utilisant Streamlit, un framework python pour créer des applications de data science et de machine learning. Cette application utilise le modèle d'IA MixTraL-8x7B-Instruct-v0.1, développé par MistralAI, pour aider les utilisateurs dans leur processus de candidature.

## Fonctionnalités

- **Score de correspondance**: Évaluer la correspondance entre un CV et une offre d'emploi en attribuant un score sur 100 et en identifiant les points forts et les points faibles.
- **Rédaction de lettre de motivation**: Générer une lettre de motivation personnalisée en fonction du CV et de l'offre d'emploi.
- **Amélioration de CV**: Améliorer un CV en intégrant les compétences, qualifications et expériences pertinentes pour l'offre d'emploi visée.

## Installation

1. Clonez le dépôt GitHub sur votre machine locale.
2. Créez un environnement virtuel et activez-le.
3. Installez les dépendances requises en exécutant `pip install -r requirements.txt`.
4. Obtenez une clé API pour HuggingFace et stockez-la dans un fichier `.env` à la racine du projet avec la clé `huggingface_api_key`.

## Exécution

Pour exécuter l'application, exécutez la commande suivante à la racine du projet :

```
streamlit run app.py
```

L'application sera alors accessible dans votre navigateur web à l'adresse `http://localhost:8501`.

## Tests

Les tests unitaires sont écrits en utilisant le framework `pytest`. Pour exécuter les tests, exécutez la commande suivante à la racine du projet :

```
pytest
```

## Structure du projet

- `app.py`: Le fichier principal qui contient le code de l'application Streamlit.
- `scr/models.py`: Contient les modèles d'IA utilisés par l'application.
- `scr/utils.py`: Contient des fonctions utilitaires pour extraire du texte à partir de fichiers PDF et DOCX.
- `tests/`: Contient les fichiers de test pour les différents composants de l'application.

## Contributions

Les contributions à ce projet sont les bienvenues. Si vous avez des idées d'amélioration, des corrections de bugs ou de nouvelles fonctionnalités, n'hésitez pas à soumettre une pull request.

## Licence

Ce projet est sous licence [MIT](LICENSE).
```