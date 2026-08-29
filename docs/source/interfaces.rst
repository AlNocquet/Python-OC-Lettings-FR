Interfaces de programmation
===========================

Le projet n'expose pas d'API REST. Les interfaces sont des routes HTTP Django
qui rendent des pages HTML côté serveur.

Routes
------

.. list-table::
   :header-rows: 1
   :widths: 28 30 42

   * - Route
     - Vue
     - Rôle
   * - ``/``
     - ``oc_lettings_site.views.index``
     - Page d'accueil
   * - ``/lettings/``
     - ``lettings.views.index``
     - Liste des locations
   * - ``/lettings/<letting_id>/``
     - ``lettings.views.letting``
     - Détail d'une location
   * - ``/profiles/``
     - ``profiles.views.index``
     - Liste des profils
   * - ``/profiles/<username>/``
     - ``profiles.views.profile``
     - Détail d'un profil
   * - ``/admin/``
     - Django Admin
     - Administration des données

Namespaces
----------

Les routes métier utilisent les namespaces ``lettings`` et ``profiles``.

Erreurs HTTP
------------

Le projet définit des handlers personnalisés :

* ``handler404`` vers ``oc_lettings_site.views.error_404`` ;
* ``handler500`` vers ``oc_lettings_site.views.error_500``.

Les templates ``404.html`` et ``500.html`` renvoient les codes HTTP correspondants.
