Démarrage rapide
================

Une fois l'environnement installé et activé :

.. code-block:: bash

   python manage.py migrate
   python manage.py runserver

Ouvrir ``http://localhost:8000``.

Navigation
----------

* ``/`` : accueil ;
* ``/lettings/`` : liste des locations ;
* ``/profiles/`` : liste des profils ;
* ``/admin/`` : administration Django.

Qualité et tests
----------------

.. code-block:: bash

   flake8 .
   pytest
   coverage run -m pytest
   coverage report

La configuration impose un seuil minimal de couverture de 80 %.
