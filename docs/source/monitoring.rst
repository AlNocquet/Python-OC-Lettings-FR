Journalisation et Sentry
========================

Journalisation Django
---------------------

La configuration ``LOGGING`` envoie les messages applicatifs vers la console.

Loggers :

* ``oc_lettings_site`` ;
* ``lettings`` ;
* ``profiles``.

Événements journalisés :

* page d'accueil ;
* listes et détails ;
* page 404 personnalisée ;
* page 500 personnalisée.

Niveaux
-------

``INFO``
    Navigation applicative utile au diagnostic.

``WARNING``
    Événement anormal non fatal, par exemple une 404.

``ERROR``
    Erreur serveur, notamment le rendu de la 500.

Sentry
------

Sentry est initialisé lorsque ``SENTRY_DSN`` est défini et que ``DEBUG=False``.
L'intégration Django est utilisée et ``send_default_pii=False``.

Le DSN ne doit jamais être versionné.

Validation
----------

Pour vérifier Sentry sur un environnement contrôlé :

#. provoquer une erreur connue ;
#. vérifier la page 500 personnalisée ;
#. vérifier l'événement dans Sentry ;
#. vérifier la journalisation côté serveur.

Ne pas conserver de route de test dédiée dans la version finale.
