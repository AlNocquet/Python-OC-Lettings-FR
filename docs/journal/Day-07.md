# Day 07 - Dependency modernization
# Jour 07 - Modernisation des dépendances

**Date:** 2026-08-24

## EN - Objectives

- Modernize the project dependencies.
- Upgrade Django while keeping compatibility with Python 3.10.
- Remove obsolete compatibility dependencies.
- Add the coverage tool required for the testing phase.
- Verify that the upgrade introduces no regression.

## EN - Work completed

The dependency stack was updated to:

- Django 5.2.17
- Flake8 7.3.0
- pytest 9.1.1
- pytest-django 4.14.0
- coverage 7.15.4

The obsolete `six` dependency was removed.

`DEFAULT_AUTO_FIELD` was configured as:

`django.db.models.AutoField`

This preserves the historical primary-key behavior of the existing project and prevents unnecessary schema migrations after upgrading Django.

## EN - Validation

The upgraded environment was validated with:

- `python manage.py check` -> no issues
- `python manage.py makemigrations --check --dry-run` -> no changes detected
- `pytest` -> 11 tests passed
- `flake8 .` -> no violations
- `pip check` -> no broken requirements

The project also continued to pass all tests after `six` was physically uninstalled from the virtual environment.

## EN - Next steps

- Create a dedicated test/coverage branch.
- Measure the current test coverage.
- Add unit, integration and functional tests where required.
- Reach more than 80% coverage with a safety margin.

---

## FR - Objectifs

- Moderniser les dépendances du projet.
- Mettre à jour Django tout en restant compatible avec Python 3.10.
- Supprimer les dépendances de compatibilité devenues obsolètes.
- Ajouter l'outil de couverture nécessaire à la phase de tests.
- Vérifier que la mise à jour n'introduit aucune régression.

## FR - Travail réalisé

Les dépendances ont été mises à jour vers :

- Django 5.2.17
- Flake8 7.3.0
- pytest 9.1.1
- pytest-django 4.14.0
- coverage 7.15.4

La dépendance obsolète `six` a été supprimée.

`DEFAULT_AUTO_FIELD` a été configuré avec :

`django.db.models.AutoField`

Cela permet de conserver le comportement historique des clés primaires du projet et d'éviter la création de migrations de schéma inutiles après la mise à jour de Django.

## FR - Validation

Le nouvel environnement a été validé avec :

- `python manage.py check` -> aucun problème
- `python manage.py makemigrations --check --dry-run` -> aucun changement détecté
- `pytest` -> 11 tests réussis
- `flake8 .` -> aucune violation
- `pip check` -> aucune dépendance cassée

Le projet continue également de réussir tous ses tests après la désinstallation réelle de `six` dans l'environnement virtuel.

## FR - Prochaines étapes

- Créer une branche dédiée aux tests et à la couverture.
- Mesurer la couverture actuelle.
- Ajouter les tests unitaires, d'intégration et fonctionnels nécessaires.
- Dépasser 80 % de couverture avec une marge de sécurité.
