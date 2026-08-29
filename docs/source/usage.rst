Guide d'utilisation
===================

Consulter une location
----------------------

#. Ouvrir la page d'accueil.
#. Accéder à la liste des locations.
#. Sélectionner une location.
#. Consulter son titre et son adresse.

Consulter un profil
-------------------

#. Ouvrir la page d'accueil.
#. Accéder à la liste des profils.
#. Sélectionner un utilisateur.
#. Consulter les informations de son profil.

Administrer les données
-----------------------

#. Ouvrir ``/admin/``.
#. S'authentifier avec un compte administrateur.
#. Gérer les objets disponibles dans Django Admin.
#. Vérifier que le rendu public reste cohérent.

Vérifier la qualité
-------------------

.. code-block:: bash

   python manage.py check
   flake8 .
   pytest
   coverage run -m pytest
   coverage report

Tester l'image Docker
---------------------

.. code-block:: bash

   docker pull alnq/oc-lettings:latest
   docker run --rm --env-file .env -p 8000:8000 alnq/oc-lettings:latest

Vérifier ensuite la page d'accueil, ``/admin/`` et les fichiers statiques.
