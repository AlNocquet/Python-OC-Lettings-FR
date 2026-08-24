# Day 08 - Test organization and coverage
# Jour 08 - Organisation des tests et couverture

**Date:** 2026-08-24

## EN - Objectives

- Review the relevance of the existing test suite.
- Add explicit unit tests for application models.
- Organize tests by unit, integration and functional categories.
- Preserve the existing pytest configuration.
- Measure application code coverage accurately.
- Enforce the required minimum coverage threshold.
- Verify that the test refactoring preserves code quality and documentation.

## EN - Work completed

The test suite was reorganized into dedicated categories while keeping tests close to their respective applications:

- `lettings/tests/unit/`
- `lettings/tests/integration/`
- `profiles/tests/unit/`
- `profiles/tests/integration/`
- `oc_lettings_site/tests/integration/`
- `oc_lettings_site/tests/functional/`

The existing `setup.cfg` was intentionally left unchanged.

Because pytest is configured with:

`python_files = tests.py`

each test category uses a `tests.py` file so that automatic test discovery remains compatible with the original project configuration.

Five explicit model unit tests were added:

- Address string representation
- Letting string representation
- Address plural name
- Profile string representation
- User-to-Profile reverse relation

Two representative functional browsing journeys were also added:

- home page -> lettings list -> letting detail
- home page -> profiles list -> profile detail

The final test suite contains:

- 5 unit tests
- 11 integration tests
- 2 functional tests
- 18 tests in total

A `.coveragerc` file was added to make coverage measurement reproducible.

Coverage is configured to:

- measure the `lettings`, `profiles` and `oc_lettings_site` applications
- exclude migrations
- exclude test files
- display missing lines
- enforce a minimum coverage threshold of 80%

All newly created Python packages, modules, classes and functions were documented with docstrings.

A complete AST-based audit confirmed that every Python module, class and function outside excluded directories has a docstring.

## EN - Validation

The final test and quality checks produced:

- `pytest` -> 18 tests passed
- `flake8 .` -> no violations
- Python docstring audit -> no missing docstrings
- `coverage run -m pytest` -> 18 tests passed
- `coverage report` -> 93% application coverage

All measured business code in models, URLs and views is covered at 100%.

The only uncovered files are Django server entry points:

- `oc_lettings_site/asgi.py`
- `oc_lettings_site/wsgi.py`

The configured 80% minimum threshold is therefore exceeded with a comfortable safety margin.

## EN - Next steps

- Integrate Sentry.
- Configure Django logging.
- Add strategic application logs.
- Move sensitive configuration values to environment variables.
- Document the logging and Sentry configuration.

---

## FR - Objectifs

- Vérifier la pertinence de la suite de tests existante.
- Ajouter des tests unitaires explicites pour les modèles des applications.
- Organiser les tests par catégories unitaires, d'intégration et fonctionnels.
- Conserver la configuration pytest existante.
- Mesurer précisément la couverture du code applicatif.
- Imposer le seuil minimal de couverture demandé.
- Vérifier que la réorganisation des tests conserve la qualité et la documentation du code.

## FR - Travail réalisé

La suite de tests a été réorganisée en catégories dédiées tout en conservant les tests au plus près de leurs applications respectives :

- `lettings/tests/unit/`
- `lettings/tests/integration/`
- `profiles/tests/unit/`
- `profiles/tests/integration/`
- `oc_lettings_site/tests/integration/`
- `oc_lettings_site/tests/functional/`

Le fichier `setup.cfg` existant a volontairement été conservé sans modification.

Pytest étant configuré avec :

`python_files = tests.py`

chaque catégorie utilise un fichier `tests.py` afin de conserver la découverte automatique des tests avec la configuration d'origine du projet.

Cinq tests unitaires explicites des modèles ont été ajoutés :

- représentation textuelle de Address
- représentation textuelle de Letting
- nom pluriel de Address
- représentation textuelle de Profile
- relation inverse entre User et Profile

Deux parcours fonctionnels représentatifs ont également été ajoutés :

- page d'accueil -> liste des locations -> détail d'une location
- page d'accueil -> liste des profils -> détail d'un profil

La suite finale contient :

- 5 tests unitaires
- 11 tests d'intégration
- 2 tests fonctionnels
- 18 tests au total

Un fichier `.coveragerc` a été ajouté afin de rendre la mesure de couverture reproductible.

La couverture est configurée pour :

- mesurer les applications `lettings`, `profiles` et `oc_lettings_site`
- exclure les migrations
- exclure les fichiers de tests
- afficher les lignes non couvertes
- imposer un seuil minimal de couverture de 80 %

Tous les nouveaux packages, modules, classes et fonctions Python ont été documentés avec des docstrings.

Un audit complet basé sur l'AST a confirmé qu'aucun module, aucune classe et aucune fonction Python hors dossiers exclus ne manque de docstring.

## FR - Validation

Les contrôles finaux de tests et de qualité donnent :

- `pytest` -> 18 tests réussis
- `flake8 .` -> aucune violation
- audit des docstrings Python -> aucune docstring manquante
- `coverage run -m pytest` -> 18 tests réussis
- `coverage report` -> 93 % de couverture applicative

Tout le code métier mesuré dans les modèles, les URL et les vues est couvert à 100 %.

Les seuls fichiers non couverts sont les points d'entrée serveur Django :

- `oc_lettings_site/asgi.py`
- `oc_lettings_site/wsgi.py`

Le seuil minimal configuré à 80 % est donc dépassé avec une marge de sécurité confortable.

## FR - Prochaines étapes

- Intégrer Sentry.
- Configurer la journalisation Django.
- Ajouter des logs applicatifs aux endroits stratégiques.
- Déplacer les valeurs de configuration sensibles vers des variables d'environnement.
- Documenter la configuration de la journalisation et de Sentry.
