Architecture
============

Organisation générale
---------------------

``oc_lettings_site``
    Configuration globale du projet Django, routage racine, page d'accueil,
    gestion des erreurs 404/500, paramètres, WSGI et ASGI.

``lettings``
    Application métier responsable des adresses et des locations.

``profiles``
    Application métier responsable des profils utilisateurs.

Arborescence simplifiée
-----------------------

.. code-block:: text

   Python-OC-Lettings-FR/
   ├── manage.py
   ├── oc_lettings_site/
   ├── lettings/
   │   ├── models.py
   │   ├── views.py
   │   ├── urls.py
   │   ├── templates/lettings/
   │   ├── migrations/
   │   └── tests/
   ├── profiles/
   │   ├── models.py
   │   ├── views.py
   │   ├── urls.py
   │   ├── templates/profiles/
   │   ├── migrations/
   │   └── tests/
   ├── templates/
   ├── static/
   ├── Dockerfile
   └── .github/workflows/ci-cd.yml

Refactorisation et migrations
-----------------------------

L'application historique regroupait les modèles dans ``oc_lettings_site``.
La refactorisation a séparé ``Address`` et ``Letting`` vers ``lettings`` et
``Profile`` vers ``profiles``.

Les données existantes sont conservées avec des migrations Django
``migrations.RunPython``. Les modèles historiques sont récupérés avec
``apps.get_model`` ; aucune requête SQL brute n'est nécessaire.

L'ordre logique est :

#. création des nouvelles tables ;
#. copie des données en conservant identifiants et relations ;
#. suppression des anciens modèles après transfert.

Routage
-------

Le routage racine reste dans ``oc_lettings_site/urls.py`` et délègue aux
applications avec ``include``. Les namespaces métier sont ``lettings`` et
``profiles``.

Fichiers statiques
------------------

Les ressources partagées restent dans ``static/``. En production,
``collectstatic`` les rassemble dans ``STATIC_ROOT`` et WhiteNoise les sert.

Serveur de production
---------------------

Le conteneur lance Gunicorn sur l'application WSGI
``oc_lettings_site.wsgi:application``. ``runserver`` est réservé au développement.
