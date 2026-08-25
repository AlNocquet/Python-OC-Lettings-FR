# Day 10 - Docker containerization
# Jour 10 - Conteneurisation Docker

**Date:** 2026-08-25

## EN - Objectives

- Prepare the local environment to run Docker containers.
- Containerize the Django application.
- Preserve the existing SQLite data migration path inside the container.
- Serve the application with a production-oriented WSGI server.
- Serve Django static files correctly from the container.
- Validate the complete Docker execution flow without introducing regressions.

## EN - Work completed

Docker Desktop was installed and configured on the development workstation.

Hardware virtualization was enabled in the BIOS and Docker Desktop successfully started its Linux engine through WSL2.

The Docker engine was validated with `docker info`.

The application was prepared for containerized execution with two additional dependencies:

- `gunicorn==26.2.0`
- `whitenoise==6.12.0`

WhiteNoise middleware was added immediately after Django's `SecurityMiddleware` so that collected static files can be served by the application.

A `.dockerignore` file was created to exclude development and sensitive files from the Docker build context, including:

- Git metadata
- the local virtual environment
- Python cache files
- pytest and coverage artifacts
- generated static files
- local `.env` files

The tracked `oc-lettings-site.sqlite3` database is deliberately included in the Docker image.

This preserves the historical database state supplied with the project and allows the existing Django data migrations to transfer its data into the refactored `lettings` and `profiles` applications when the container starts.

A Dockerfile was created using `python:3.10-slim`.

The container startup sequence performs:

1. Django database migrations with `python manage.py migrate --noinput`
2. static file collection with `python manage.py collectstatic --noinput`
3. application startup with Gunicorn on `0.0.0.0:8000`

Environment variables are supplied at runtime rather than copied into the Docker image.

The local container can therefore be started with the existing `.env` file using a single `docker run` command.

The Docker image was successfully built with the local tag:

`oc-lettings:local`

The container was then launched successfully and the complete startup sequence was validated.

All pending project migrations were applied inside the container, including the migrations responsible for moving the historical data into the new applications.

Django successfully collected 149 static files.

Gunicorn started successfully and exposed the application on port 8000.

## EN - Validation

The Docker implementation was validated with:

- `docker info` -> Docker Linux engine operational through WSL2
- `docker build -t oc-lettings:local .` -> image built successfully
- container startup -> successful
- database migrations -> successful
- `collectstatic` -> 149 static files collected
- Gunicorn -> started successfully on port 8000
- home page -> HTTP 200
- Django admin -> HTTP 200
- Django admin CSS -> HTTP 200
- `python manage.py check` -> no issues
- `pytest` -> 18 tests passed
- `flake8 .` -> no violations
- `coverage run -m pytest` -> 18 tests passed
- `coverage report` -> 93% application coverage

Local pytest execution reports warnings because the generated `staticfiles` directory does not exist outside the container.

This does not affect the application or the tests. Inside the Docker container, `collectstatic` creates the directory before Gunicorn starts, and the static-file delivery was validated successfully.

## EN - Next steps

- Configure the GitHub Actions CI/CD workflow.
- Run linting, tests and coverage validation automatically on pushed branches.
- Restrict Docker image build and publication to the `master` branch.
- Publish Docker images to Docker Hub with distinct version tags.
- Configure automated deployment after a successful Docker publication.
- Document the final deployment and application management procedure.

---

## FR - Objectifs

- Préparer l'environnement local pour l'exécution de conteneurs Docker.
- Conteneuriser l'application Django.
- Préserver le chemin de migration des données SQLite existantes dans le conteneur.
- Servir l'application avec un serveur WSGI adapté à une exécution déployée.
- Servir correctement les fichiers statiques Django depuis le conteneur.
- Valider l'ensemble du fonctionnement Docker sans introduire de régression.

## FR - Travail réalisé

Docker Desktop a été installé et configuré sur le poste de développement.

La virtualisation matérielle a été activée dans le BIOS et Docker Desktop a ensuite pu démarrer correctement son moteur Linux avec WSL2.

Le fonctionnement du moteur Docker a été validé avec `docker info`.

Deux dépendances supplémentaires ont été ajoutées pour permettre l'exécution conteneurisée de l'application :

- `gunicorn==26.2.0`
- `whitenoise==6.12.0`

Le middleware WhiteNoise a été ajouté immédiatement après le `SecurityMiddleware` de Django afin de permettre à l'application de servir les fichiers statiques collectés.

Un fichier `.dockerignore` a été créé afin d'exclure du contexte de construction Docker les fichiers de développement et les fichiers sensibles, notamment :

- les métadonnées Git
- l'environnement virtuel local
- les caches Python
- les artefacts pytest et coverage
- les fichiers statiques générés
- les fichiers `.env` locaux

La base versionnée `oc-lettings-site.sqlite3` est volontairement incluse dans l'image Docker.

Cela permet de conserver l'état historique de la base fourni avec le projet et d'utiliser les migrations Django existantes pour transférer ses données vers les applications refactorisées `lettings` et `profiles` au démarrage du conteneur.

Un Dockerfile basé sur `python:3.10-slim` a été créé.

La séquence de démarrage du conteneur effectue :

1. les migrations Django avec `python manage.py migrate --noinput`
2. la collecte des fichiers statiques avec `python manage.py collectstatic --noinput`
3. le démarrage de l'application avec Gunicorn sur `0.0.0.0:8000`

Les variables d'environnement sont fournies au moment de l'exécution et ne sont pas copiées dans l'image Docker.

Le conteneur local peut ainsi être lancé avec le fichier `.env` existant au moyen d'une seule commande `docker run`.

L'image Docker a été construite avec succès avec le tag local :

`oc-lettings:local`

Le conteneur a ensuite été lancé avec succès et l'ensemble de sa séquence de démarrage a été validé.

Toutes les migrations en attente ont été appliquées dans le conteneur, y compris celles responsables du transfert des données historiques vers les nouvelles applications.

Django a collecté avec succès 149 fichiers statiques.

Gunicorn a démarré correctement et expose l'application sur le port 8000.

## FR - Validation

La conteneurisation Docker a été validée avec :

- `docker info` -> moteur Docker Linux opérationnel avec WSL2
- `docker build -t oc-lettings:local .` -> image construite avec succès
- démarrage du conteneur -> réussi
- migrations de la base de données -> réussies
- `collectstatic` -> 149 fichiers statiques collectés
- Gunicorn -> démarré correctement sur le port 8000
- page d'accueil -> HTTP 200
- administration Django -> HTTP 200
- feuille CSS de l'administration Django -> HTTP 200
- `python manage.py check` -> aucun problème
- `pytest` -> 18 tests réussis
- `flake8 .` -> aucune violation
- `coverage run -m pytest` -> 18 tests réussis
- `coverage report` -> 93 % de couverture applicative

L'exécution locale de pytest affiche des avertissements car le répertoire généré `staticfiles` n'existe pas en dehors du conteneur.

Cela n'affecte ni l'application ni les tests. Dans le conteneur Docker, `collectstatic` crée ce répertoire avant le démarrage de Gunicorn et la distribution des fichiers statiques a été validée avec succès.

## FR - Prochaines étapes

- Configurer le workflow CI/CD GitHub Actions.
- Exécuter automatiquement le lint, les tests et la validation de couverture sur les branches poussées.
- Réserver la construction et la publication des images Docker à la branche `master`.
- Publier les images Docker sur Docker Hub avec des tags de version distincts.
- Configurer le déploiement automatisé après publication réussie de l'image Docker.
- Documenter la procédure finale de déploiement et de gestion de l'application.
