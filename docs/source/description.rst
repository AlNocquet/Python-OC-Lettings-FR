Description du projet
=====================

Orange County Lettings est une application web Django permettant de consulter des
locations et des profils utilisateurs.

Le Projet 13 consiste à reprendre une application existante afin de réduire sa dette
technique et de l'industrialiser. Le travail réalisé couvre notamment :

* la séparation des responsabilités métier en applications Django dédiées ;
* la conservation des données historiques grâce aux migrations Django ;
* l'amélioration de la qualité du code ;
* la mise en place de pages d'erreur personnalisées ;
* l'ajout de tests unitaires, d'intégration et fonctionnels ;
* la mesure de la couverture de tests ;
* la journalisation applicative ;
* l'intégration de Sentry ;
* la conteneurisation avec Docker ;
* une chaîne CI/CD avec GitHub Actions ;
* la publication des images sur Docker Hub ;
* le déploiement sur Render ;
* la publication de la documentation avec Sphinx et Read the Docs.

Objectif fonctionnel
--------------------

La refactorisation conserve le comportement principal de l'application :

* afficher la page d'accueil ;
* afficher la liste et le détail des locations ;
* afficher la liste et le détail des profils ;
* conserver l'interface d'administration Django ;
* conserver le rendu visuel et les fichiers statiques en production.

Le projet n'expose pas d'API REST. Les interfaces sont des pages HTML rendues
côté serveur par Django et l'interface d'administration Django.
