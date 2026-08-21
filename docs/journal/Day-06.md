# Day 06 - Custom error pages
# Jour 06 - Pages d'erreur personnalisées

**Date:** 2026-08-21

## EN - Objectives

- Implement custom 404 and 500 error pages.
- Keep the visual identity and navigation of the existing site.
- Configure Django to use project-level custom error handlers.
- Add automated tests for error handling.
- Preserve code quality and existing application behavior.

## EN - Work completed

### Custom error handlers

Two project-level error handlers were added to `oc_lettings_site.views`:

- `error_404`
- `error_500`

The 404 handler renders `404.html` with HTTP status 404.

The 500 handler renders `500.html` with HTTP status 500.

Both functions include docstrings and comply with the existing project code-quality rules.

### URL configuration

The root URL configuration now declares:

- `handler404 = 'oc_lettings_site.views.error_404'`
- `handler500 = 'oc_lettings_site.views.error_500'`

The handlers are therefore configured at project level while the existing application routes remain unchanged.

### Error templates

Two global templates were added:

- `templates/404.html`
- `templates/500.html`

Both templates extend the existing `base.html` template.

This preserves:

- the existing navigation bar;
- the Orange County Lettings visual identity;
- the existing CSS and static resources;
- access back to the home page.

The 404 page informs the user that the requested page could not be found.

The 500 page informs the user that an unexpected internal error occurred.

### Automated tests

A new `oc_lettings_site/tests.py` module was added with three meaningful tests.

The tests verify:

1. The custom 404 and 500 handlers are configured in the root URL configuration.
2. An unknown URL returns HTTP 404 and renders the custom `404.html` template when `DEBUG=False`.
3. The custom 500 handler returns HTTP 500 and renders the expected error content.

The 404 test explicitly disables Django debug mode in order to validate the custom production-style error handling behavior.

### Validation

Targeted error tests:

- 3 tests passed

Complete project validation:

- `pytest` -> 11 tests passed
- `flake8 .` -> no violations
- `python manage.py check` -> no issues

No regression was introduced into the existing lettings or profiles functionality.

## EN - Next steps

- Expand model tests.
- Measure the current test coverage.
- Add tests where necessary to exceed 80% coverage.
- Continue with logging and Sentry integration.

---

## FR - Objectifs

- Implémenter des pages d'erreur 404 et 500 personnalisées.
- Conserver l'identité visuelle et la navigation du site existant.
- Configurer Django pour utiliser des gestionnaires d'erreurs personnalisés au niveau du projet.
- Ajouter des tests automatisés pour la gestion des erreurs.
- Préserver la qualité du code et le fonctionnement existant de l'application.

## FR - Travail réalisé

### Gestionnaires d'erreurs personnalisés

Deux gestionnaires d'erreurs ont été ajoutés dans `oc_lettings_site.views` :

- `error_404`
- `error_500`

Le gestionnaire 404 affiche `404.html` avec le statut HTTP 404.

Le gestionnaire 500 affiche `500.html` avec le statut HTTP 500.

Les deux fonctions disposent de docstrings et respectent les règles de qualité du code déjà mises en place dans le projet.

### Configuration des URLs

La configuration principale des URLs déclare désormais :

- `handler404 = 'oc_lettings_site.views.error_404'`
- `handler500 = 'oc_lettings_site.views.error_500'`

Les gestionnaires sont ainsi configurés au niveau du projet sans modifier les routes existantes des applications.

### Templates d'erreur

Deux templates globaux ont été ajoutés :

- `templates/404.html`
- `templates/500.html`

Les deux héritent du template existant `base.html`.

Cela permet de conserver :

- la barre de navigation existante ;
- l'identité visuelle Orange County Lettings ;
- les feuilles de style et ressources statiques existantes ;
- un accès permettant de revenir à la page d'accueil.

La page 404 indique que la page demandée est introuvable.

La page 500 indique qu'une erreur interne inattendue est survenue.

### Tests automatisés

Un nouveau module `oc_lettings_site/tests.py` a été ajouté avec trois tests utiles.

Les tests vérifient :

1. La configuration des gestionnaires personnalisés 404 et 500 dans le routage principal.
2. Le retour HTTP 404 et le rendu du template personnalisé `404.html` pour une URL inexistante avec `DEBUG=False`.
3. Le retour HTTP 500 et le contenu attendu du gestionnaire personnalisé 500.

Le test 404 désactive explicitement le mode debug de Django afin de vérifier le comportement personnalisé correspondant aux conditions de production.

### Validation

Tests ciblés des erreurs :

- 3 tests réussis

Validation complète du projet :

- `pytest` -> 11 tests réussis
- `flake8 .` -> aucune violation
- `python manage.py check` -> aucun problème

Aucune régression n'a été introduite dans les fonctionnalités existantes de lettings ou profiles.

## FR - Prochaines étapes

- Étendre les tests des modèles.
- Mesurer la couverture actuelle des tests.
- Ajouter les tests nécessaires pour dépasser 80 % de couverture.
- Poursuivre avec la journalisation et l'intégration de Sentry.
