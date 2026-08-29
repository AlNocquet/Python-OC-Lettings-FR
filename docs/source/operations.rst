Gestion et exploitation
=======================

Démarrage local
---------------

.. code-block:: bash

   python manage.py migrate
   python manage.py runserver

Créer un administrateur
-----------------------

.. code-block:: bash

   python manage.py createsuperuser

Ne jamais inscrire les identifiants dans le README ou le code.

Migrations
----------

Vérifier l'absence de changement de schéma inattendu :

.. code-block:: bash

   python manage.py makemigrations --check --dry-run

Appliquer les migrations :

.. code-block:: bash

   python manage.py migrate

Fichiers statiques
------------------

.. code-block:: bash

   python manage.py collectstatic --noinput

WhiteNoise sert les fichiers collectés en production.

Contrôles avant livraison
-------------------------

.. code-block:: bash

   python manage.py check
   flake8 .
   pytest
   coverage run -m pytest
   coverage report

Règles de déploiement
---------------------

Une branche autre que ``master`` s'arrête après le job de tests.

Un push sur ``master`` peut atteindre la production uniquement si le linting,
les tests, la couverture, le build Docker et la publication Docker réussissent.

Vérifications de production
---------------------------

#. ouvrir la page d'accueil ;
#. vérifier les locations et les profils ;
#. ouvrir ``/admin/`` ;
#. vérifier les CSS statiques ;
#. consulter les logs Render si nécessaire ;
#. consulter Sentry en cas d'erreur.

Persistance
-----------

Le projet utilise SQLite. Sur un hébergement au système de fichiers éphémère,
les modifications réalisées directement en production peuvent disparaître lors
d'un redéploiement. Pour des données durables en production, une base externe
persistante serait préférable.
