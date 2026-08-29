Installation
============

Prérequis
---------

* Python 3.10
* Git
* pip
* Docker Desktop si l'image Docker doit être exécutée localement

Clonage
-------

.. code-block:: bash

   git clone https://github.com/AlNocquet/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR

Environnement virtuel
---------------------

Windows PowerShell :

.. code-block:: powershell

   python -m venv venv
   .\venv\Scripts\Activate.ps1

macOS / Linux :

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate

Dépendances
-----------

.. code-block:: bash

   pip install -r requirements.txt

Variables d'environnement
--------------------------

Créer ``.env`` à partir de ``.env.example`` :

.. code-block:: text

   DJANGO_SECRET_KEY=<clé-secrète-locale>
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
   SENTRY_DSN=

Le fichier ``.env`` ne doit jamais être versionné.

Base de données
---------------

.. code-block:: bash

   python manage.py migrate
   python manage.py check
