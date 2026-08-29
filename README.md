# Orange County Lettings

Application web Django de consultation de locations et de profils, refactorisée dans le cadre du Projet 13 OpenClassrooms.

Le projet réduit la dette technique de l'application existante, sépare les responsabilités métier en applications Django dédiées et industrialise les tests, la conteneurisation et le déploiement grâce à une chaîne CI/CD.

## Liens

- Dépôt GitHub : https://github.com/AlNocquet/Python-OC-Lettings-FR
- Pipeline GitHub Actions : https://github.com/AlNocquet/Python-OC-Lettings-FR/actions
- Application en production : https://oc-lettings-9le6.onrender.com
- Image Docker Hub : https://hub.docker.com/r/alnq/oc-lettings
- Documentation Read the Docs : **à remplacer par l'URL publique après import du dépôt**

## Architecture

Le projet comporte trois composants principaux :

- `oc_lettings_site` : configuration globale, accueil, routage principal et pages d'erreur ;
- `lettings` : modèles `Address` et `Letting`, vues, URLs, templates et tests associés ;
- `profiles` : modèle `Profile`, vues, URLs, templates et tests associés.

Les fichiers statiques communs restent dans `static/`. En production, `collectstatic` les rassemble dans `staticfiles/` et WhiteNoise les sert.

## Prérequis

- Python 3.10
- Git
- pip
- Docker Desktop pour exécuter l'image Docker

## Installation locale

```bash
git clone https://github.com/AlNocquet/Python-OC-Lettings-FR.git
cd Python-OC-Lettings-FR
python -m venv venv
```

Sous Windows PowerShell :

```powershell
.\venv\Scripts\Activate.ps1
```

Sous macOS / Linux :

```bash
source venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Créer `.env` à partir de `.env.example` :

```text
DJANGO_SECRET_KEY=<clé-secrète-locale>
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
SENTRY_DSN=
```

Ne jamais versionner `.env`.

Appliquer les migrations et lancer le site :

```bash
python manage.py migrate
python manage.py runserver
```

Site : `http://localhost:8000`
Admin : `http://localhost:8000/admin/`

Utiliser un compte administrateur configuré localement. Aucun identifiant ou mot de passe ne doit être stocké dans le dépôt.

## Contrôles qualité

```bash
python manage.py check
flake8 .
pytest
coverage run -m pytest
coverage report
```

Le seuil minimal de couverture est de 80 %.

## Documentation Sphinx

```bash
pip install -r docs/requirements.txt
```

macOS / Linux :

```bash
cd docs
make html
```

Windows PowerShell :

```powershell
cd docs
.\make.bat html
```

La documentation est générée dans `docs/build/html/`.

## Déploiement

### Fonctionnement général

```text
Push GitHub
    |
    v
CI : lint + tests + couverture
    |
    | master uniquement
    v
CD : build Docker
    |
    v
Docker Hub
    |
    v
Deploy hook Render
    |
    v
Production
```

Sur toutes les branches, GitHub Actions exécute linting, tests et couverture.

Sur `master` uniquement, si ces contrôles réussissent :

1. construction de l'image Docker ;
2. publication sur Docker Hub avec le SHA complet du commit et `latest` ;
3. appel du deploy hook Render ;
4. déploiement de l'image correspondant au SHA.

### Configuration requise

Secrets GitHub Actions :

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
- `RENDER_DEPLOY_HOOK`

Variables Render :

```text
DJANGO_SECRET_KEY=<secret>
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=<nom-hôte-render>
SENTRY_DSN=<dsn-sentry>
PORT=8000
```

Les secrets ne doivent jamais être inscrits dans le dépôt.

### Docker

Le conteneur applique les migrations, collecte les statiques et démarre Gunicorn sur le port 8000.

```bash
docker pull alnq/oc-lettings:latest
docker run --rm --env-file .env -p 8000:8000 alnq/oc-lettings:latest
```

Pour reproduire une version précise, utiliser le tag SHA du commit.

### Fichiers statiques

`collectstatic` rassemble les ressources dans `STATIC_ROOT`, puis WhiteNoise les sert en production. Le site et l'admin doivent conserver le même rendu qu'en local.

### Base de données

Le projet utilise SQLite. Les migrations sont exécutées au démarrage du conteneur.

Sur un hébergement dont le système de fichiers est éphémère, les modifications de données réalisées en production ne sont pas garanties après redéploiement. Une base externe persistante serait préférable pour une application de production durable.

### Journalisation et Sentry

Django journalise les événements applicatifs pour `oc_lettings_site`, `lettings` et `profiles`.

Sentry est initialisé lorsque `SENTRY_DSN` est défini et que `DEBUG=False`. `send_default_pii=False` évite l'envoi de données personnelles par défaut.

### Vérification après déploiement

Vérifier :

1. les jobs GitHub Actions ;
2. l'état `Live` sur Render ;
3. la page d'accueil ;
4. `/admin/` ;
5. les fichiers statiques ;
6. Sentry en cas de test d'erreur.

## Read the Docs

Après import du dépôt GitHub dans Read the Docs :

1. utiliser `.readthedocs.yaml` ;
2. lancer le premier build ;
3. vérifier l'URL publique ;
4. vérifier qu'un nouveau push déclenche automatiquement un nouveau build ;
5. remplacer le placeholder Read the Docs dans ce README par l'URL publique.

## Contexte

Projet réalisé dans le cadre du parcours OpenClassrooms.
