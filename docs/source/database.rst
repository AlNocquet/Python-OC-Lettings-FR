Base de données et modèles
==========================

Moteur
------

Le projet utilise SQLite, configuré dans ``oc_lettings_site/settings.py``.

Modèle ``Address``
------------------

Application : ``lettings``

* ``number`` : entier positif, maximum 9999 ;
* ``street`` : chaîne de 64 caractères maximum ;
* ``city`` : chaîne de 64 caractères maximum ;
* ``state`` : code sur 2 caractères ;
* ``zip_code`` : entier positif, maximum 99999 ;
* ``country_iso_code`` : code pays ISO sur 3 caractères.

Modèle ``Letting``
------------------

Application : ``lettings``

* ``title`` : titre, 256 caractères maximum ;
* ``address`` : relation ``OneToOneField`` vers ``Address`` avec suppression en cascade.

Modèle ``Profile``
------------------

Application : ``profiles``

* ``user`` : relation ``OneToOneField`` vers ``django.contrib.auth.models.User`` ;
* ``favorite_city`` : chaîne de 64 caractères maximum, facultative.

Relations
---------

.. code-block:: text

   Address 1 ───── 1 Letting
   Django User 1 ───── 1 Profile

Migration des données historiques
---------------------------------

Les données existantes sont transférées avec des migrations Django ``RunPython``.
Les modèles historiques sont chargés avec ``apps.get_model`` pour respecter
l'état du schéma au moment de chaque migration. Le transfert ne repose pas sur
du SQL brut.
