# Day 03 - Routing, views, templates and admin refactoring
# Jour 03 - Refactorisation du routage, des vues, des templates et de l'administration

**Date:** 2026-08-21

## EN - Objectives

- Complete the move of application-specific views and routing into `lettings` and `profiles`.
- Introduce URL namespaces without changing the public URLs.
- Move application templates into their respective Django apps.
- Move Django admin registration to the new applications.
- Add tests covering the refactored routing and views.

## EN - Work completed

The Lettings and Profiles views were moved into their dedicated applications.

The former list views were renamed:

- `lettings_index` -> `lettings.views.index`
- `profiles_index` -> `profiles.views.index`

Dedicated URL configurations were created:

- `lettings/urls.py`
- `profiles/urls.py`

Application namespaces were introduced:

- `lettings:index`
- `lettings:letting`
- `profiles:index`
- `profiles:profile`

The project-level URL configuration now delegates application routing with `include()` while preserving the existing public paths.

Templates were moved into application-specific directories:

- `lettings/templates/lettings/index.html`
- `lettings/templates/lettings/letting.html`
- `profiles/templates/profiles/index.html`
- `profiles/templates/profiles/profile.html`

Template URL references were updated to use the new namespaces.

Django admin registration was moved from `oc_lettings_site` to the respective `lettings` and `profiles` applications.

## EN - Validation

`python manage.py check` reports no issues.

URL reversal confirms that the public paths remain unchanged:

- `/`
- `/lettings/`
- `/lettings/1/`
- `/profiles/`
- `/profiles/HeadlinesGazer/`

Functional requests return HTTP 200 for all tested pages.

The Django admin registry contains only the new domain models:

- `lettings.Address`
- `lettings.Letting`
- `profiles.Profile`

Dedicated tests were added for Lettings and Profiles routing and views.

Full test suite result:

- 9 tests collected
- 9 tests passed

## EN - Next steps

- Remove the legacy models and database tables through Django migrations.
- Remove the temporary `related_name='+'` workaround from the new Profile model.
- Continue with code quality, docstrings, error handling and broader test coverage.

---

## FR - Objectifs

- Terminer le déplacement des vues et du routage métier vers `lettings` et `profiles`.
- Introduire les namespaces d'URL sans modifier les URLs publiques.
- Déplacer les templates dans leurs applications Django respectives.
- Déplacer l'enregistrement de l'administration Django vers les nouvelles applications.
- Ajouter des tests couvrant le routage et les vues refactorisés.

## FR - Travail réalisé

Les vues Lettings et Profiles ont été déplacées dans leurs applications dédiées.

Les anciennes vues de liste ont été renommées :

- `lettings_index` -> `lettings.views.index`
- `profiles_index` -> `profiles.views.index`

Des configurations d'URL dédiées ont été créées :

- `lettings/urls.py`
- `profiles/urls.py`

Les namespaces applicatifs ont été introduits :

- `lettings:index`
- `lettings:letting`
- `profiles:index`
- `profiles:profile`

La configuration principale des URLs délègue désormais le routage aux applications avec `include()` tout en conservant les chemins publics existants.

Les templates ont été déplacés dans les répertoires propres aux applications :

- `lettings/templates/lettings/index.html`
- `lettings/templates/lettings/letting.html`
- `profiles/templates/profiles/index.html`
- `profiles/templates/profiles/profile.html`

Les références d'URL dans les templates ont été adaptées aux nouveaux namespaces.

L'enregistrement dans l'administration Django a été déplacé de `oc_lettings_site` vers les applications `lettings` et `profiles`.

## FR - Validation

`python manage.py check` ne signale aucune erreur.

La résolution inverse des URLs confirme que les chemins publics sont inchangés :

- `/`
- `/lettings/`
- `/lettings/1/`
- `/profiles/`
- `/profiles/HeadlinesGazer/`

Les requêtes fonctionnelles testées retournent toutes un statut HTTP 200.

Le registre de l'administration Django contient uniquement les nouveaux modèles métier :

- `lettings.Address`
- `lettings.Letting`
- `profiles.Profile`

Des tests dédiés au routage et aux vues Lettings et Profiles ont été ajoutés.

Résultat de la suite complète :

- 9 tests collectés
- 9 tests réussis

## FR - Prochaines étapes

- Supprimer les anciens modèles et les anciennes tables au moyen des migrations Django.
- Retirer le `related_name='+'` temporaire du nouveau modèle Profile.
- Poursuivre avec la qualité du code, les docstrings, la gestion des erreurs et l'extension de la couverture de tests.
