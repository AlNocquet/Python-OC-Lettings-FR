# Day 02 - Application split and data migration
# Jour 02 - Séparation des applications et migration des données

**Date:** 2026-08-20

## EN - Objectives

- Split the monolithic Django application into `lettings` and `profiles`.
- Preserve all existing business data through Django migrations.
- Validate the migration before removing any legacy model or table.

## EN - Work completed

Created and registered the `lettings` and `profiles` applications.

New model locations:

- `Address` and `Letting` -> `lettings`
- `Profile` -> `profiles`

The legacy models remain temporarily available during the transition.

A temporary `related_name='+'` was added to the new `Profile.user` relation to avoid a reverse-accessor conflict while both Profile models coexist.

Created schema migrations and explicit `RunPython` data migrations. No direct SQL was used.

The migration preserves:

- primary keys;
- `Letting.address_id` relationships;
- `Profile.user_id` relationships.

The migration strategy is documented in ADR-001.

## EN - Validation

`python manage.py migrate --plan` confirmed the expected migration order.

All migrations were applied successfully.

Data verification:

- Addresses: 6 legacy / 6 new
- Lettings: 6 legacy / 6 new
- Profiles: 4 legacy / 4 new
- Address data comparison: identical
- Letting data and relationships: identical
- Profile data and relationships: identical

No legacy table has been removed yet.

## EN - Next steps

- Move views, URLs, templates and admin configuration into the new applications.
- Remove the temporary Profile relation workaround.
- Remove legacy models and tables through Django migrations.
- Add dedicated tests for the refactored architecture.

---

## FR - Objectifs

- Séparer l'application Django monolithique en `lettings` et `profiles`.
- Préserver toutes les données métier existantes au moyen des migrations Django.
- Valider la migration avant toute suppression de modèle ou de table historique.

## FR - Travail réalisé

Création et déclaration des applications `lettings` et `profiles`.

Nouvelle répartition des modèles :

- `Address` et `Letting` -> `lettings`
- `Profile` -> `profiles`

Les anciens modèles restent temporairement disponibles pendant la transition.

Un `related_name='+'` temporaire a été ajouté à la nouvelle relation `Profile.user` afin d'éviter un conflit d'accès inverse pendant la coexistence des deux modèles Profile.

Création des migrations de schéma et de migrations de données explicites avec `RunPython`. Aucun SQL direct n'a été utilisé.

La migration conserve :

- les clés primaires ;
- les relations `Letting.address_id` ;
- les relations `Profile.user_id`.

La stratégie de migration est documentée dans l'ADR-001.

## FR - Validation

`python manage.py migrate --plan` a confirmé l'ordre attendu des migrations.

Toutes les migrations ont été appliquées avec succès.

Vérification des données :

- Adresses : 6 anciennes / 6 nouvelles
- Locations : 6 anciennes / 6 nouvelles
- Profils : 4 anciens / 4 nouveaux
- Données Address : identiques
- Données et relations Letting : identiques
- Données et relations Profile : identiques

Aucune ancienne table n'a encore été supprimée.

## FR - Prochaines étapes

- Déplacer les vues, URLs, templates et la configuration admin vers les nouvelles applications.
- Retirer l'ajustement temporaire de la relation Profile.
- Supprimer les anciens modèles et les anciennes tables via les migrations Django.
- Ajouter les tests dédiés à l'architecture refactorisée.
