# simplonEnMieux

Un projet Flask pour démontrer comment structurer une application web simple avec migrations et base de données.

## 🚀 Installation

1. Clone le dépôt et positionne-toi sur la branche `main` :

```bash
git clone https://github.com/olivierLegendre/simplonEnMieux.git
cd simplonEnMieux
git checkout main
```

2. Crée un environnement virtuel et installe les dépendances :

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🧰 Usage

Avant de lancer l’application Flask, configure les variables d’environnement :

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

Pour démarrer le serveur :

```bash
flask run
```

Ensuite, ouvre ton navigateur sur l’URL affichée (généralement `http://127.0.0.1:5000`).

## ⚙️ Gestion de la base de données

Le projet utilise Flask-Migrate (Alembic) pour gérer les migrations. Voici les commandes utiles :

```bash
flask db init        # Initialiser les migrations (à faire une seule fois)
flask db migrate -m "Nom de la migration"
flask db upgrade     # Appliquer les migrations à la base de données
```

## 📁 Structure du projet

```
simplonEnMieux/
├── app.py           # Point d’entrée de l’application
├── migrations/      # Dossier des migrations (auto-généré)
├── project/         # (à documenter : modèles, views, etc.)
├── requirements.txt # Dépendances Python
├── .gitignore
└── LICENSE
```

## 📦 Dépendances

Voici un aperçu des dépendances principales (vérifie `requirements.txt` pour les versions exactes) :

- Flask
- Flask-Migrate
- SQLAlchemy (utilisé sous le capot)

Ajoute toute autre dépendance spécifique à ton projet ici.

## 🧪 Tests (optionnel)

Indique ici la procédure pour lancer les tests si le projet en contient (ex : `pytest`).

## 🤝 Contribution

Les contributions sont les bienvenues! Pour proposer des modifications, utilise les pull requests. Merci de respecter le format de commit et d’ajouter des tests (si disponibles).

## 📄 Licence

Ce projet est sous licence **MIT** – voir le fichier `LICENSE` pour les détails.
