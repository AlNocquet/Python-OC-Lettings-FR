# Day 04 - Legacy models and tables removal
# Jour 04 - Suppression des anciens modèles et tables

**Date:** 2026-08-21

## EN - Objectives

- Complete the architectural split by removing the legacy business models from `oc_lettings_site`.
- Delete the obsolete legacy database tables through Django migrations.
- Guarantee that migrated data is preserved before any deletion.
- Remove the temporary Profile relationship workaround.

## EN - Work completed

Before deletion, the legacy and new data were compared again:

- Legacy Addresses: 6
- New Addresses: 6
- Legacy Lettings: 6
- New Lettings: 6
- Legacy Profiles: 4
- New Profiles: 4

The legacy `Address`, `Letting` and `Profile` model definitions were removed from `oc_lettings_site.models`.

Django generated a migration to:

- remove the legacy `Letting.address` relation;
- remove the legacy `Profile.user` relation;
- delete the legacy `Address` model;
- delete the legacy `Letting` model;
- delete the legacy `Profile` model.

Explicit dependencies were added to ensure that:

- `lettings.0002_migrate_existing_data`
- `profiles.0002_migrate_existing_data`

must complete before the legacy tables can be removed.

This guarantees the migration order:

1. Create new tables.
2. Copy existing data.
3. Delete legacy tables.

No direct SQL or manual database manipulation was used.

After the legacy Profile model was removed, the temporary `related_name='+'` workaround was removed from the new `profiles.Profile.user` relation.

A final Django migration records the standard `OneToOneField` relationship.

## EN - Validation

The legacy table removal migration was applied successfully.

Database verification after deletion:

- Addresses: 6
- Lettings: 6
- Profiles: 4
- Legacy `oc_lettings_site_*` business tables: none

The standard reverse Django relationship was restored successfully:

- `user.profile` -> working

Final validation:

- `python manage.py check` -> no issues
- full pytest suite -> 9 tests passed

The legacy business layer has now been completely removed from `oc_lettings_site`.

## EN - Next steps

- Continue with code quality and Flake8 cleanup.
- Add required docstrings.
- Implement proper 404 and 500 error handling.
- Expand the test suite and measure coverage.

---

## FR - Objectifs

- Terminer la séparation de l'architecture en supprimant les anciens modèles métier de `oc_lettings_site`.
- Supprimer les anciennes tables devenues inutiles au moyen des migrations Django.
- Garantir la conservation des données migrées avant toute suppression.
- Retirer l'ajustement temporaire de la relation Profile.

## FR - Travail réalisé

Avant toute suppression, les anciennes et nouvelles données ont de nouveau été comparées :

- Anciennes adresses : 6
- Nouvelles adresses : 6
- Anciennes locations : 6
- Nouvelles locations : 6
- Anciens profils : 4
- Nouveaux profils : 4

Les anciennes définitions des modèles `Address`, `Letting` et `Profile` ont été supprimées de `oc_lettings_site.models`.

Django a généré une migration permettant de :

- supprimer l'ancienne relation `Letting.address` ;
- supprimer l'ancienne relation `Profile.user` ;
- supprimer l'ancien modèle `Address` ;
- supprimer l'ancien modèle `Letting` ;
- supprimer l'ancien modèle `Profile`.

Des dépendances explicites ont été ajoutées afin de garantir que :

- `lettings.0002_migrate_existing_data`
- `profiles.0002_migrate_existing_data`

soient obligatoirement terminées avant la suppression des anciennes tables.

L'ordre de migration est ainsi garanti :

1. Création des nouvelles tables.
2. Copie des données existantes.
3. Suppression des anciennes tables.

Aucun SQL direct ni aucune manipulation manuelle de la base de données n'a été utilisé.

Après suppression de l'ancien modèle Profile, le `related_name='+'` temporaire a été retiré de la relation `profiles.Profile.user`.

Une migration Django finale enregistre le retour à la relation `OneToOneField` standard.

## FR - Validation

La migration supprimant les anciennes tables a été appliquée avec succès.

Vérification de la base après suppression :

- Adresses : 6
- Locations : 6
- Profils : 4
- Anciennes tables métier `oc_lettings_site_*` : aucune

La relation inverse Django standard a été rétablie avec succès :

- `user.profile` -> fonctionnel

Validation finale :

- `python manage.py check` -> aucune erreur
- suite pytest complète -> 9 tests réussis

L'ancienne couche métier a maintenant été entièrement retirée de `oc_lettings_site`.

## FR - Prochaines étapes

- Poursuivre avec la qualité du code et le nettoyage Flake8.
- Ajouter les docstrings requises.
- Implémenter la gestion correcte des erreurs 404 et 500.
- Étendre la suite de tests et mesurer la couverture.
