Projet Poly#
============

Décrire brièvement le projet ici.

Le fichier `README.md` est écrit en [**Markdown**](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) et permet de soigner la _mise en forme_.

Fonctionnement du projet
========================

L'utilisation est très simple, les maps étants dans `./input/`, on utilise la commande python suivante :

`python3 polyhash.py ./input/<map>`

Example sous linux : 

`python3 polyhash.py input/a_an_example.in.txt`


Le résultat sortira alors dans `./output.txt`

La fonction `solve` dans `solver.py` choisis automatiquement la meilleure stratégie.

L'équipe
========

- Erwan Brunelliere: erwan.brunelliere@etu.univ-nantes.fr
- Gabriel Comte: gabriel.comte@etu.univ-nantes.fr
- allan guillard : allan.guillard@etu.univ-nantes.fr
- Evan Godec : evan.godec@etu.univ-nantes.fr

Descriptif du projet
====================

Le but est de déplacer le père noël de manière à ce qu’il puisse distribuer le maximum de cadeau dans un temps imparti. Pour cela sa maison se situe au point (0,0) de chaque map. Pour que le Père Noël se déplace nous pouvons donner des carottes aux reines, cela permet d'accélérer le Père Noël. Son accélération est limitée en fonction de son poids (plus il est lourd plus l'accélération possible diminue). Le poid du Père Noël se calcule par la somme des poids des cadeaux qu’il portent et des carottes (une carotte= 1 kilo). L’accélération du Père Noël peut se faire que sur un seul axe à la fois x ou y. Certes l’accélération du Père Noël est finie néanmoins sa vitesse est infinie. 
Lorsque le Père Noël se déplace le temps s’incrémente de 1 néanmoins le chargement de cadeau ou le dépôts de cadeaux ne compte pas de temps supplémentaire.
Le Père Noël possède une range, il peut alors livrer les cadeaux dans la range autour de lui.

répartition des tâches/fonctions du projet au sein de l'équipe
===============================================================

Pour la répartition nous avons:
- Erwan Brunellière et Gabriel Comte: Développeur de stratégie. Rôle responsable de coder les stratégies permettant de naviguer et déposer les cadeaux de manière optimisée.
- Allan Guillard: Développeur de la Visualisation. Rôle responsable de coder dans un premier temps l’affichage (avant que le site nous le permette) puis l’affichage de groupe de cadeau.
- Evan Godec: Développeur Déplacement. Rôle responsable de coder la première fonction de déplacement du Père Noël sur un point précis.

procédure d'installation
========================

`import de matplotlib.pyplot`
`import de math`
`import de print`


procédure d'exécution
=====================

`python3 polyhash.py input/nom_du_fichier`

détail de la/des stratégie.s mise.s en oeuvre et commentaire à propos des performances (temps d'exécution et place mémoire)
===========================================================================================================================

_stratégie ligne droite :_



_stratégie cluster :_
La stratégie de cluster a pour but de creéer dans la map des packets de cadeaux raproché comme nous poucons l'avoir dans la map b (4 packets de cadeau ou cluster) ou d (29 packets de cadeau ou cluster). Pour cela dans un premier temps nous découpons la map en plusieurs carré d'environ même dimension (la difficulté étant pour les bords de droites et du bas car nous commençons en haut a gauche). Une fois la map découpé en plusieurs sous-map nous faisons la moyenne de distance des points contenues dans chaque sous map puis nous faisons une moyenne de la moyenne de distance des points dans chaque sous map. Cette moyenne de moyenne nous permet d'avoir une distance moyenne réaliste séparant chaque cadeaux qui sont déjà proche. Cette moyenne nous permettra alors de faciliter la création de cluster. 
Une fois la moyenne de moyenne calculé on passe a la création de cluster alors on créer une liste qui stockera tous les cluster (qui sont des listes de cadeaux). Pour chaque cadeau: 
- s'il n'est pas déjà dans un cluster on créée un nouveau cluster et on ajoute tous ses cadeaux qui sont à une distance qui est la distance moyenne calculé précedement.
- si le cadeau est déjà dans un cluster alors on récupère le cluster existant et on ajoute ses cadeaux qui sont autour de lui (avec une distance égale à la distance moyenne calculé précédement).
Maintenant que les clusters sont remplis, pour chaque cluster nous allons calculé le chemin le plus court. Pour cela nous récupérons le cadeau le plus proche du pére du cluster, nous mettons ce cadeau dans une liste puis depuis ce cadeau nous ajoutons son cadeau le plus proche et ainsi de suite jusqu'a avoir tous les cadeaux du cluster dans la liste trier.
Nous avons enfin tous les composants pour commencer à faire naviguer le Père Noël avec cette stratégies. Pour cela nous vérifions dans un premier temps si nous sommes sur le point (0,0) si oui alors on fait le plein de cadeaux et de carottes. Tant que le poid tu Père Noël est inférieur au poid maximum (que nous définissons) alors on continue de prendre des cadeaux mais si nous dépassons alors nous ne prenons pas le cadeaux qui nous fait dépasser puis nous comblons le poid tu Père Noël avec des carottes. Enfin une fois charger le Père Noël part livrer les cadeaux tout en vérifiant si une fois arriver au prochain cadeau il aura assez de carotte pour revenir en (0,0). Si on a plus assez de carotte alors on revient en (0,0) refaire le plein de cadeau et de carotte. Nous faisons cela pour tous les clusters de la map jusqu'a ce que ce que le temps du Père Noël vaut le temps maximal de la Map.


bugs et limitations connu.e.s
=============================

_bugs et limitation pour le cluster_
 