from Map import Map
from utils import get_distance, diviseur


class Zone:
    """
    La classe zone a pour but la création de cluster sur chacune des maps
    """

    def __init__(self, gifts:list):
        """
        gifts: listd de cadeau
        cluster: une liste de cadeau regroupé sur la map
        list_ration: la liste des ratio point poid pour chaque cluster 
        """
        self.gifts = gifts
        self.cluster=[]
        self.list_ratio=[]


    def moyenne_points(self,map:Map,santa):
        """
        Découpe la vraie map en plusieurs petite sous-map où l'on calcul la moyenne de
        distance des points pour chaque sous map.
        Retourne la moyenne de la moyenne de distance des points pour chaque sous-map
        """
        #On découpe la map en plusieur sous-map dans un tabelau
        list_scale=map.split_in_scale(santa.taille_map//10) #le diviseur à été décidé comme cela car ça nous paraissé réaliste pour toute les map
        list_moyenne=[]
        #pour chaque carré en calcul la moyenne de distance entre un point et tous les points qui sont dans la sous map pour tous les points et toutes les sou map
        for scale in list_scale:
            list_gift=[]
            for gift in self.gifts:
                if scale.in_scale(gift.x,gift.y):
                    list_gift.append(gift)
            for gift_1 in list_gift:
                somme=0
                if len(list_gift)>1:
                    for gift_2 in list_gift:
                        somme=somme+get_distance(gift_1.x, gift_1.y, gift_2.x, gift_2.y)
                    list_moyenne.append(somme/(len(list_gift)-1))
        somme_moyenne=0
        #pour chaque moyenne total de sous map on fait la moyenne de toutes les sous map pour avoir une moyenne de distance de chaque cadeau dans la map
        for moyenne in list_moyenne:
            somme_moyenne=somme_moyenne+moyenne

        #si on arrive pas a avoir de moyenne alors de base la moyenne de distance sera de 10 
        if(len(list_moyenne)==0):
            return 10
        return int(somme_moyenne/len(list_moyenne))+santa.taille_map//(santa.taille_map//diviseur(santa.taille_map))

    
    def clusterisation(self,distance_moyenne):
        """
        Création des clusters
        distance_moyenne: la moyenne de distance des points sur la map (obtenue par la méthode: moyenne_points)
        """
        #Un cluster se créer par rapport à la distance moyenne des cadeaux dans la map
        list_cluster=[]
        #pour chaque cadeaux
        for gift_1 in self.gifts:
            list_courante=[]
            for list_c in list_cluster:
                #s'il est déja dans un cluster alors on récpère le cluster pour retravailler dessus car un cadeaux ne peux pas se trouver dans 2 clusters différents
                if gift_1 in list_c:
                    list_courante=list_c
                    list_cluster.remove(list_c)
                    break;
            #pour tous les autres cadeau
            for gift_2 in self.gifts:
                #s'il n'est pas déjà dans le cluster car nous ne souhaitons pas avoir de doublons
                if(gift_2 not in list_courante):
                    if (gift_2.x in range(gift_1.x-distance_moyenne,gift_1.x+distance_moyenne) and gift_2.y in range(gift_1.y-distance_moyenne,gift_1.y+distance_moyenne)):
                        #on met le cadeau dans le cluster
                        list_courante.append(gift_2)
            #si la liste courante est vide c'est à dire qu'aucun cluster ne contient le cadeau
            if(list_courante==[]):
                list_courante.append(gift_1)
            list_cluster.append(list_courante)
        list_cluster_temp=list_cluster
        for list_c1 in list_cluster:
            for list_c2 in list_cluster:
                if (list_c1[0] in list_c2 and list_c1!=list_c2):
                    list_cluster_temp.remove(list_c2)
        list_cluster=list_cluster_temp
        self.cluster=list_cluster
        return list_cluster

    
    def calcul_score_total_cluster(self):
        """
        Calcule le score total d'un cluster
        """
        list_score=[]
        for cluster in self.cluster:
            somme_score_cluster=0
            for gift in cluster:
                somme_score_cluster=somme_score_cluster+gift.score
            list_score.append(somme_score_cluster)
        return list_score


    def cacul_ratio_par_cluster(self):
        """
        calcul de ratio poid point de chaque cluster et les ajoutes à la liste de ratio
        """
        list_ratio=[]
        for cluster in self.cluster:
            ratio = 0
            weight = 0
            for gift in cluster:
                ratio = ratio+ gift.ratio
                weight = weight+gift.weight
            list_ratio.append(ratio / len(cluster))
        self.list_ratio=list_ratio
        return list_ratio
