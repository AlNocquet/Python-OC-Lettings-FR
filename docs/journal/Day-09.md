# Day 09 - Environment, Sentry and application logging
# Jour 09 - Environnement, Sentry et journalisation applicative

**Date:** 2026-08-24

## EN - Objectives

- Move sensitive Django configuration out of the source code.
- Provide a reproducible environment-variable configuration.
- Integrate Sentry error monitoring.
- Prevent local development and automated tests from polluting Sentry monitoring.
- Configure Django application logging.
- Add strategic logs without exposing sensitive user data.
- Validate the complete configuration without introducing regressions.

## EN - Work completed

Environment configuration was introduced with `python-dotenv`.

A versioned `.env.example` file now documents the required configuration variables:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `SENTRY_DSN`

Local `.env` and `.env.local` files are ignored by Git.

Django now loads the following settings from environment variables:

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`

The local development secret key was regenerated instead of reusing the previously hard-coded value.

The Sentry SDK was added and integrated into Django.

The Sentry DSN is loaded exclusively from the environment. Sentry initialization occurs only when:

- a `SENTRY_DSN` is configured
- Django is running with `DEBUG=False`

This prevents local development and automated tests from sending events to the production monitoring project.

Default personally identifiable information is disabled with:

`send_default_pii=False`

A dedicated Sentry project was created for OC Lettings.

The integration was validated with a real Sentry event successfully received by the dedicated project.

Django application logging was also configured with:

- console output
- timestamps
- severity levels
- logger names
- dedicated loggers for `oc_lettings_site`, `lettings` and `profiles`

Strategic logging was added to application views:

- `INFO` for home-page requests
- `INFO` for lettings list and detail requests
- `INFO` for profiles list and detail requests
- `WARNING` for custom 404 responses
- `ERROR` for custom 500 responses

No usernames, requested URLs, secrets or other sensitive user data are included in application log messages.

During manual logging validation, the tracked local SQLite database was found to still represent the historical pre-refactoring migration state.

The database was deliberately left unchanged.

Application logging for `lettings` and `profiles` was therefore validated through pytest's temporary migrated test database rather than modifying the tracked SQLite file.

## EN - Validation

The complete configuration was validated with:

- `python manage.py check` -> no issues
- `pytest` -> 18 tests passed
- integration logging tests -> 8 tests passed with expected INFO output
- `flake8 .` -> no violations
- `coverage run -m pytest` -> 18 tests passed
- `coverage report` -> 93% application coverage

Application view modules remain fully covered:

- `lettings/views.py` -> 100%
- `profiles/views.py` -> 100%
- `oc_lettings_site/views.py` -> 100%

Sentry no longer attempts to send events while the test suite runs with debug mode enabled.

## EN - Next steps

- Containerize the application with Docker.
- Validate that the site can run locally from the Docker image.
- Configure CI/CD with automated tests, linting and coverage validation.
- Build and publish versioned Docker images.
- Configure automated deployment from the `master` branch.

---

## FR - Objectifs

- Sortir la configuration sensible Django du code source.
- Fournir une configuration reproductible par variables d'environnement.
- Intégrer le suivi des erreurs avec Sentry.
- Éviter que le développement local et les tests automatisés ne polluent le suivi Sentry.
- Configurer la journalisation applicative Django.
- Ajouter des logs stratégiques sans exposer de données utilisateur sensibles.
- Valider l'ensemble de la configuration sans introduire de régression.

## FR - Travail réalisé

La gestion des variables d'environnement a été mise en place avec `python-dotenv`.

Un fichier `.env.example` versionné documente désormais les variables nécessaires :

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `SENTRY_DSN`

Les fichiers locaux `.env` et `.env.local` sont ignorés par Git.

Django charge désormais depuis les variables d'environnement :

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`

La clé secrète utilisée pour le développement local a été régénérée au lieu de réutiliser l'ancienne valeur codée en dur.

Le SDK Sentry a été ajouté et intégré à Django.

Le DSN Sentry est chargé exclusivement depuis l'environnement. Sentry est initialisé uniquement lorsque :

- un `SENTRY_DSN` est configuré
- Django fonctionne avec `DEBUG=False`

Cela évite que le développement local et les tests automatisés n'envoient des événements vers le projet de supervision.

L'envoi par défaut des informations personnelles identifiables est désactivé avec :

`send_default_pii=False`

Un projet Sentry dédié à OC Lettings a été créé.

L'intégration a été validée avec un véritable événement Sentry reçu avec succès par ce projet dédié.

La journalisation applicative Django a également été configurée avec :

- sortie console
- horodatage
- niveaux de gravité
- nom du logger
- loggers dédiés pour `oc_lettings_site`, `lettings` et `profiles`

Des logs stratégiques ont été ajoutés aux vues :

- `INFO` pour la consultation de la page d'accueil
- `INFO` pour les listes et détails des locations
- `INFO` pour les listes et détails des profils
- `WARNING` pour les réponses personnalisées 404
- `ERROR` pour les réponses personnalisées 500

Aucun nom d'utilisateur, URL demandée, secret ou autre donnée utilisateur sensible n'est inclus dans les messages de log applicatifs.

Lors de la validation manuelle du logging, la base SQLite locale versionnée a été identifiée comme étant encore dans son état historique antérieur à la refactorisation des migrations.

Cette base a volontairement été laissée inchangée.

La journalisation des applications `lettings` et `profiles` a donc été validée avec la base temporaire migrée créée par pytest, sans modifier le fichier SQLite suivi par Git.

## FR - Validation

L'ensemble de la configuration a été validé avec :

- `python manage.py check` -> aucun problème
- `pytest` -> 18 tests réussis
- validation du logging d'intégration -> 8 tests réussis avec les logs INFO attendus
- `flake8 .` -> aucune violation
- `coverage run -m pytest` -> 18 tests réussis
- `coverage report` -> 93 % de couverture applicative

Les modules de vues applicatives restent entièrement couverts :

- `lettings/views.py` -> 100 %
- `profiles/views.py` -> 100 %
- `oc_lettings_site/views.py` -> 100 %

Sentry ne tente plus d'envoyer d'événements lorsque la suite de tests fonctionne avec le mode debug activé.

## FR - Prochaines étapes

- Conteneuriser l'application avec Docker.
- Vérifier que le site peut fonctionner localement depuis l'image Docker.
- Configurer la CI/CD avec tests, lint et validation de couverture automatisés.
- Construire et publier des images Docker versionnées.
- Configurer le déploiement automatisé depuis la branche `master`.
