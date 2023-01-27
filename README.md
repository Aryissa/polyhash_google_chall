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

**stratégie ligne droite :**
Il y a 3 strétégies de ligne droite disponibles. Elle commencent du plus simple au plus complexe.

Chaque stratégie commence par avancer dans l'axe des x, on pourrait commencer par y, certaines fonctions sont prévues pour mais pas toutes.

**La premiere**va sur une ligne droite à vitesse constante et ditribue exactement sur une ligne.
Elle permet d'utiliser exactement 8 carottes.
On regarde si un cadeau est sur la droites de de vecteur (a, b) grace à l'equation 
`x + (b / a) * gift.x + b == y + gift.y`

Elle utilise 3 fonctions.

**line** permet d'énumérer les demies-droites avec pour chacune leur vecteur et la liste des cadeaux qui sont exactement dessus.

**lines_actions** permet de simuler l'action que fera le père noël, ainsi décider quels cadeaux prendre et combien de temps ça prendra.

**lines_navigate_x** permet de réaliser les mouvements du père noël.

**La Deuxieme** fonctionne exactement comma la premiere, à l'exception qu'elle distribue avec sa distance de distribution.
On regarde si le cadeau se situe entre deux droites. Celle de la premiere +- la distance.

Donc l'équation `y + gift.y + self.game.range >= x_res >= y + gift.y - self.game.range`

Elle utilise 3 fonctions :

* line_r
* lines_r_actions
* lines_r_navigate_x

**La Troisième** quant à elle, accelère tout au long. Pour réaliser une ligne droite, on accélère deux fois de suite dans chaque direction. Ensuite on décelère exatement dans le même ordre pour revenir à la vitesse 0.

Elle utilise 5 fonctions :
* **find_nb_accel** qui calcule le nombre d'acceleration pour atteindre le dernier cadeau avant de faire demi tour
* line_r
* line_rs_actions
* line_rs_navigate_x
* lines_rs_return_x



**stratégie cluster :**
La stratégie de cluster a pour but de creéer dans la map des packets de cadeaux raproché comme nous poucons l'avoir dans la map b (4 packets de cadeau ou cluster) ou d (29 packets de cadeau ou cluster). Pour cela dans un premier temps nous découpons la map en plusieurs carré d'environ même dimension (la difficulté étant pour les bords de droites et du bas car nous commençons en haut a gauche). Une fois la map découpé en plusieurs sous-map nous faisons la moyenne de distance des points contenues dans chaque sous map puis nous faisons une moyenne de la moyenne de distance des points dans chaque sous map. Cette moyenne de moyenne nous permet d'avoir une distance moyenne réaliste séparant chaque cadeaux qui sont déjà proche. Cette moyenne nous permettra alors de faciliter la création de cluster. 
Une fois la moyenne de moyenne calculé on passe a la création de cluster alors on créer une liste qui stockera tous les cluster (qui sont des listes de cadeaux). Pour chaque cadeau: 
- s'il n'est pas déjà dans un cluster on créée un nouveau cluster et on ajoute tous ses cadeaux qui sont à une distance qui est la distance moyenne calculé précedement.
- si le cadeau est déjà dans un cluster alors on récupère le cluster existant et on ajoute ses cadeaux qui sont autour de lui (avec une distance égale à la distance moyenne calculé précédement).
Maintenant que les clusters sont remplis, pour chaque cluster nous allons calculé le chemin le plus court. Pour cela nous récupérons le cadeau le plus proche du pére du cluster, nous mettons ce cadeau dans une liste puis depuis ce cadeau nous ajoutons son cadeau le plus proche et ainsi de suite jusqu'a avoir tous les cadeaux du cluster dans la liste trier.
Nous avons enfin tous les composants pour commencer à faire naviguer le Père Noël avec cette stratégies. Pour cela nous vérifions dans un premier temps si nous sommes sur le point (0,0) si oui alors on fait le plein de cadeaux et de carottes. Tant que le poid tu Père Noël est inférieur au poid maximum (que nous définissons) alors on continue de prendre des cadeaux mais si nous dépassons alors nous ne prenons pas le cadeaux qui nous fait dépasser puis nous comblons le poid tu Père Noël avec des carottes. Enfin une fois charger le Père Noël part livrer les cadeaux tout en vérifiant si une fois arriver au prochain cadeau il aura assez de carotte pour revenir en (0,0). Si on a plus assez de carotte alors on revient en (0,0) refaire le plein de cadeau et de carotte. Nous faisons cela pour tous les clusters de la map jusqu'a ce que ce que le temps du Père Noël vaut le temps maximal de la Map.

description de l'organisation du code (en packages, modules, classes, fonctions)
================================================================================
Tout d’abord, nous avons créé une classe Gift avec les attribut associé, soit le nom, le poids, son score ainsi que sa position en x et en y. 
Par la suite, nous avons donc créé la classe Santa pour symboliser notre père noël. Pour se faire, nous lui avons implémenté quelques attributs qui changent au fur et à mesure que le code s'exécute. 
Ses attributs sont donc : 
- son poids actuel ( cadeaux plus les carottes )
- sa position
- sa vitesse
- le nombre de carottes qu’il possède ainsi que sa liste de cadeaux en sa possession.

Une fois ces attributs mis en place, nous lui avons créé quelques fonctions : 
- Charger dans sa hotte des carottes et des cadeaux ( ici, les cadeaux sont retiré de la liste générale puis stocker dans une liste temporaire le temps d’être livré )
- Pouvoir livrer les cadeaux ( ce qui les retire de sa liste de cadeaux embarqué dans sa hotte )
- Connaître l'accélération maximum à laquelle il peut aller grâce à son poids actuel. 
- La fonction add_output permet de retranscrire les actions du père noël sous forme de texte afin de se faire évaluer par l’arbitre. 
- Les fonctions affichages quant à elles permettent l’affichage des différentes maps ainsi que de vecteurs de déplacements du père noël. 

Nous avons aussi créé une classe game qui permet de recuperer toute les donnée de chaque jeu de donnée, soit : 
- le temps maximum
- le temps actuel
- la distance maximum a lequel le père noël peut livrer les cadeaux
- les accélérations possibles en fonctions du poids
- le nombres de gift total

Puis pour finir, celle qui nous aura pris le plus de temps fut celle de la navigation. En effet, c’est dans celle-ci que toutes nos solutions sont retranscrites. Pour se faire, ici, Nous avons aussi plusieurs fonctions : 
- La fonction go_point_slow qui permet d’aller à un point avec une vitesse maximale très limitée. 
- La fonction go_point, qui reprend la fonction précédente sans limite de vitesse. 
- les fonctions predict_carrots, qui nous ont permis de prédire combien de carottes seront nécessaires pour faire l’aller retour. 
- chemin_kruskal, qui nous a permis de trier la liste et de savoir quels cadeaux allez déposer en premier pour avoir le chemin le plus court.
- Deplacements_cluster qui dépend de la classe cluster, dans laquelle les cadeaux sont regroupés par paquet puis trier par groupe du plus intéressant (en fonction du poids, de la distance et de scores) au moins intéressant. Cette fonction permet donc de se déplacer dans les  clusters. 
line


bugs et limitations connu.e.s
=============================
Il y a une limite connue de tous les codes que nous possédons, suite à une mauvaise compréhension des consignes l'accélération maximales est aussi la vitesse maximale c'est à dire que si l'accélération max est à 16 alors nous pourrons pas aller plus vite que la vitesse 16


**bugs et limitation pour le cluster**
Du côté de l'algorithme de cluster il ne fonctionne pas suite à une érreur un possible qui est transmi depuis une autre méthode de déplacement qu'on ne comprennais pas. Son score pour la map b est d'environ 6100 points. C'est pour cette limitation très forte qu'on a pas pu intégrer la solution de cluster.

