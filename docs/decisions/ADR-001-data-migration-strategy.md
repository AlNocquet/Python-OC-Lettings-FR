# ADR-001 - Data migration strategy for application split
# ADR-001 - Stratégie de migration des données pour la séparation des applications

**Status / Statut:** Accepted / Accepté
**Date:** 2026-08-20

## EN - Context

The initial project stores the `Address`, `Letting`, and `Profile` models in the monolithic `oc_lettings_site` application.

The project specifications require the architecture to be split into:

- `lettings`, containing `Address` and `Letting`;
- `profiles`, containing `Profile`.

Existing database data must be preserved. The specifications require the new tables to be populated through Django migrations without using direct SQL, and the old tables must subsequently be removed through Django migrations.

Initial business data:

- 6 addresses
- 6 lettings
- 4 profiles

## EN - Decision

The migration will be performed in explicit stages:

1. Create the `lettings` and `profiles` applications.
2. Create the new models and their database tables.
3. Use Django data migrations with `RunPython` to copy existing records into the new tables.
4. Preserve primary keys and existing relationships during the copy.
5. Verify record counts and relationships after migration.
6. Update the application to use the new models.
7. Remove the legacy models and tables using Django migrations.

Direct SQL and manual database manipulation will not be used.

## EN - Rationale

This approach follows the OpenClassrooms specifications directly and keeps the migration history explicit and reproducible.

Using Django historical models through the migration framework also avoids coupling the migration to the current application code.

## EN - Consequences

During the transition, old and new tables will temporarily coexist.

The old tables will only be removed after the copied data has been verified and the application has been switched to the new models.

This slightly increases the number of migration steps but reduces the risk of data loss.

---

## FR - Contexte

Le projet initial stocke les modèles `Address`, `Letting` et `Profile` dans l'application monolithique `oc_lettings_site`.

Le cahier des charges demande de séparer l'architecture en deux applications :

- `lettings`, contenant `Address` et `Letting` ;
- `profiles`, contenant `Profile`.

Les données existantes de la base doivent être conservées. Les nouvelles tables doivent être alimentées au moyen des migrations Django, sans SQL direct, puis les anciennes tables doivent être supprimées au moyen des migrations Django.

Données métier initiales :

- 6 adresses
- 6 locations
- 4 profils

## FR - Décision

La migration sera réalisée en plusieurs étapes explicites :

1. Créer les applications `lettings` et `profiles`.
2. Créer les nouveaux modèles et leurs nouvelles tables.
3. Utiliser des migrations de données Django avec `RunPython` pour copier les enregistrements existants.
4. Conserver les clés primaires et les relations existantes pendant la copie.
5. Vérifier le nombre d'enregistrements et les relations après migration.
6. Faire utiliser les nouveaux modèles par l'application.
7. Supprimer les anciens modèles et les anciennes tables au moyen des migrations Django.

Aucun SQL direct ni aucune manipulation manuelle de la base de données ne seront utilisés.

## FR - Justification

Cette approche respecte directement le cahier des charges OpenClassrooms et conserve un historique de migration explicite et reproductible.

L'utilisation des modèles historiques de Django dans les migrations évite également de coupler la migration à l'état courant du code de l'application.

## FR - Conséquences

Pendant la transition, les anciennes et les nouvelles tables coexisteront temporairement.

Les anciennes tables ne seront supprimées qu'après vérification des données copiées et après bascule de l'application vers les nouveaux modèles.

Cette stratégie augmente légèrement le nombre d'étapes de migration, mais réduit le risque de perte de données.
