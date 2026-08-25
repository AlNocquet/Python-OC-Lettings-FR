# Day 11 - CI/CD pipeline and production deployment
# Jour 11 - Pipeline CI/CD et déploiement en production

**Date:** 2026-08-25

## ENG - Objectives

- Automate linting, tests and coverage validation with GitHub Actions.
- Build and publish Docker images automatically after successful validation.
- Publish uniquely tagged Docker images to Docker Hub.
- Deploy the validated Docker image to a production hosting platform.
- Restrict containerization and deployment to the `master` branch.
- Validate the complete CI/CD pipeline in real conditions.

## ENG - Work completed

A GitHub Actions workflow was created in:

`.github/workflows/ci-cd.yml`

The workflow is triggered on pushes to all branches.

The first job, `Lint, tests and coverage`, reproduces the local validation environment with Python 3.10 and:

- installs the project dependencies
- runs `flake8 .`
- runs the complete pytest suite through coverage
- checks the configured minimum coverage threshold

Dedicated CI environment variables are supplied for Django.

`DJANGO_ALLOWED_HOSTS` includes `testserver` so that Django integration and functional tests can run with `DEBUG=False`.

The coverage threshold continues to be enforced by `.coveragerc` with:

`fail_under = 80`

A second job, `Build and push Docker image`, depends on the successful completion of the test job.

This job runs only when the pushed branch is `master`.

Docker Hub credentials are stored as protected GitHub repository secrets:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

The Docker image is built with GitHub Actions and published to:

`alnq/oc-lettings`

Each successful build publishes two tags:

- `latest`
- the complete Git commit SHA

The commit SHA provides a unique and traceable Docker image for each successful production build.

The first local Docker Hub push attempts experienced repeated network timeouts.

The Docker image itself was not affected. The publication was therefore validated through the GitHub Actions runner, where the Docker build and push completed successfully.

The Docker Hub repository was verified to contain both the `latest` tag and the commit-specific SHA tag.

A Render Web Service was created from the public Docker Hub image:

`docker.io/alnq/oc-lettings:latest`

The production service uses:

- Frankfurt region
- free compute plan
- port `8000`
- health check path `/`

Production environment variables are configured directly in Render:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS`
- `SENTRY_DSN`
- `PORT=8000`

Secrets are not stored in Git, the Docker image or the GitHub Actions workflow.

The production hostname is:

`oc-lettings-9le6.onrender.com`

The first Render deployment exposed an `ALLOWED_HOSTS` mismatch because the generated Render hostname contains a unique suffix.

The production configuration was corrected to use the exact Render hostname.

After redeployment, the Render health check returned HTTP 200 and the service became live.

The deployed application was manually validated through:

- the public home page
- application static files
- the Django administration login page

The Django administration interface was correctly styled, confirming that `collectstatic` and WhiteNoise work in production.

A Render deploy hook was then stored as the protected GitHub repository secret:

`RENDER_DEPLOY_HOOK`

A third GitHub Actions job, `Deploy to Render`, was added.

This job:

- depends on the successful Docker publication job
- runs only on `master`
- calls the protected Render deploy hook
- explicitly supplies the Docker image tagged with the exact Git commit SHA

This guarantees that Render deploys the precise image produced by the same successful CI/CD execution.

## ENG - Validation

The complete CI/CD pipeline was executed successfully from a real push to `master`.

GitHub Actions validated the three jobs in sequence:

1. `Lint, tests and coverage` -> successful
2. `Build and push Docker image` -> successful
3. `Deploy to Render` -> successful

Docker Hub successfully received:

- `alnq/oc-lettings:latest`
- a Docker image tagged with the full Git commit SHA

Render recorded the final production deployment as:

- triggered via Deploy Hook
- based on the commit-specific Docker image
- successfully deployed
- live

The deployed application successfully completed:

- Django migrations
- historical data migration
- collection of 149 static files
- Gunicorn startup on port 8000
- Render health check with HTTP 200
- home-page request with HTTP 200

The public site and Django administration interface were both manually verified.

The CI/CD chain is therefore validated end to end:

Git push -> automated validation -> Docker build -> Docker Hub publication -> automated Render deployment -> live application.

## ENG - Next steps

- Complete the final project documentation.
- Document deployment and application management procedures.
- Configure and validate Read the Docs.
- Perform a final specification and repository audit.
- Prepare the project for presentation and technical review.

---

## FR - Objectifs

- Automatiser le lint, les tests et la validation de couverture avec GitHub Actions.
- Construire et publier automatiquement les images Docker après validation.
- Publier des images Docker avec des tags uniques sur Docker Hub.
- Déployer l'image Docker validée sur une plateforme de production.
- Réserver la conteneurisation et le déploiement à la branche `master`.
- Valider l'ensemble du pipeline CI/CD dans des conditions réelles.

## FR - Travail réalisé

Un workflow GitHub Actions a été créé dans :

`.github/workflows/ci-cd.yml`

Le workflow est déclenché lors des pushs sur toutes les branches.

Le premier job, `Lint, tests and coverage`, reproduit l'environnement de validation local avec Python 3.10 et :

- installe les dépendances du projet
- exécute `flake8 .`
- exécute l'ensemble de la suite pytest avec coverage
- contrôle le seuil minimal de couverture configuré

Des variables d'environnement dédiées à la CI sont fournies à Django.

`DJANGO_ALLOWED_HOSTS` inclut `testserver` afin que les tests d'intégration et fonctionnels Django puissent fonctionner avec `DEBUG=False`.

Le seuil de couverture reste imposé par `.coveragerc` avec :

`fail_under = 80`

Un deuxième job, `Build and push Docker image`, dépend de la réussite du job de tests.

Ce job est exécuté uniquement lorsque la branche poussée est `master`.

Les identifiants Docker Hub sont stockés sous forme de secrets protégés du dépôt GitHub :

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

L'image Docker est construite par GitHub Actions et publiée dans :

`alnq/oc-lettings`

Chaque construction réussie publie deux tags :

- `latest`
- le SHA Git complet du commit

Le SHA du commit fournit une image Docker unique et traçable pour chaque construction de production réussie.

Les premières tentatives de push manuel vers Docker Hub ont rencontré plusieurs timeouts réseau.

L'image Docker n'était pas en cause. La publication a donc été validée depuis le runner GitHub Actions, où la construction et le push Docker ont réussi.

Le dépôt Docker Hub a été vérifié avec les tags `latest` et le tag SHA correspondant au commit.

Un Web Service Render a été créé à partir de l'image publique Docker Hub :

`docker.io/alnq/oc-lettings:latest`

Le service de production utilise :

- la région Frankfurt
- le plan gratuit
- le port `8000`
- le chemin de health check `/`

Les variables d'environnement de production sont configurées directement dans Render :

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS`
- `SENTRY_DSN`
- `PORT=8000`

Les secrets ne sont stockés ni dans Git, ni dans l'image Docker, ni dans le workflow GitHub Actions.

Le nom d'hôte de production est :

`oc-lettings-9le6.onrender.com`

Le premier déploiement Render a révélé une incompatibilité dans `ALLOWED_HOSTS`, car le nom d'hôte généré par Render comporte un suffixe unique.

La configuration de production a été corrigée afin d'utiliser le nom d'hôte Render exact.

Après redéploiement, le health check Render a retourné un HTTP 200 et le service est passé en ligne.

L'application déployée a été validée manuellement avec :

- la page d'accueil publique
- les fichiers statiques de l'application
- la page de connexion de l'administration Django

L'administration Django était correctement mise en forme, confirmant le fonctionnement de `collectstatic` et WhiteNoise en production.

Un deploy hook Render a ensuite été enregistré comme secret protégé du dépôt GitHub :

`RENDER_DEPLOY_HOOK`

Un troisième job GitHub Actions, `Deploy to Render`, a été ajouté.

Ce job :

- dépend de la réussite du job de publication Docker
- est exécuté uniquement sur `master`
- appelle le deploy hook Render protégé
- transmet explicitement l'image Docker taguée avec le SHA exact du commit Git

Cela garantit que Render déploie précisément l'image produite par la même exécution CI/CD réussie.

## FR - Validation

Le pipeline CI/CD complet a été exécuté avec succès depuis un véritable push sur `master`.

GitHub Actions a validé les trois jobs dans l'ordre :

1. `Lint, tests and coverage` -> réussi
2. `Build and push Docker image` -> réussi
3. `Deploy to Render` -> réussi

Docker Hub a reçu avec succès :

- `alnq/oc-lettings:latest`
- une image Docker taguée avec le SHA Git complet du commit

Render a enregistré le déploiement final de production comme :

- déclenché via Deploy Hook
- basé sur l'image Docker correspondant au commit
- déployé avec succès
- en ligne

L'application déployée a exécuté avec succès :

- les migrations Django
- la migration des données historiques
- la collecte de 149 fichiers statiques
- le démarrage de Gunicorn sur le port 8000
- le health check Render avec HTTP 200
- la requête de page d'accueil avec HTTP 200

Le site public et l'interface d'administration Django ont tous deux été vérifiés manuellement.

La chaîne CI/CD est donc validée de bout en bout :

Push Git -> validation automatisée -> construction Docker -> publication Docker Hub -> déploiement Render automatisé -> application en ligne.

## FR - Prochaines étapes

- Terminer la documentation finale du projet.
- Documenter les procédures de déploiement et de gestion de l'application.
- Configurer et valider Read the Docs.
- Effectuer un audit final des spécifications et du dépôt.
- Préparer le projet pour la soutenance et la révision technique.
