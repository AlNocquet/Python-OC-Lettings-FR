Déploiement
===========

Vue d'ensemble
--------------

La chaîne CI/CD est définie dans ``.github/workflows/ci-cd.yml``.

.. code-block:: text

   Push GitHub
       |
       v
   Lint + tests + couverture
       |
       | master uniquement
       v
   Build Docker
       |
       v
   Docker Hub
       |
       v
   Deploy hook Render
       |
       v
   Production

Intégration continue — CI
-------------------------

Le job ``Lint, tests and coverage`` s'exécute sur toutes les branches :

#. checkout du dépôt ;
#. Python 3.10 ;
#. installation des dépendances ;
#. ``flake8 .`` ;
#. ``coverage run -m pytest`` ;
#. ``coverage report``.

Le seuil minimal de couverture est de 80 %.

Livraison et déploiement continus — CD
--------------------------------------

Les jobs Docker et déploiement ne s'exécutent que sur ``master``.

Le job Docker publie :

.. code-block:: text

   alnq/oc-lettings:<SHA_DU_COMMIT>
   alnq/oc-lettings:latest

Le job de déploiement transmet à Render l'image correspondant au SHA du commit.

Secrets GitHub
--------------

* ``DOCKERHUB_USERNAME``
* ``DOCKERHUB_TOKEN``
* ``RENDER_DEPLOY_HOOK``

Variables Render
----------------

.. code-block:: text

   DJANGO_SECRET_KEY=<secret>
   DJANGO_DEBUG=False
   DJANGO_ALLOWED_HOSTS=<nom-hôte-render>
   SENTRY_DSN=<dsn>
   PORT=8000

Conteneur
---------

Le conteneur exécute :

.. code-block:: bash

   python manage.py migrate --noinput
   python manage.py collectstatic --noinput
   gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000

Image publiée
-------------

.. code-block:: bash

   docker pull alnq/oc-lettings:<SHA_DU_COMMIT>
   docker run --rm --env-file .env -p 8000:8000 alnq/oc-lettings:<SHA_DU_COMMIT>

Read the Docs
-------------

Le dépôt contient ``.readthedocs.yaml``. Après import du dépôt, Read the Docs
doit reconstruire automatiquement la documentation lors des mises à jour du dépôt.
