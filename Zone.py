from Map import Map
from Gift import Gift
from utils import get_distance, diviseur

class Zone:
    def __init__(self, gifts:list):
        self.gifts = gifts
        self.cluster=[]
        #ratio = 0
        #self.weight = 0
        #for i in gifts:
            #ratio = ratio+ i.ratio
            #self.weight = self.weight+i.weight
        #self.ratio = ratio / len(gifts)
        #self.initial_gift = max(gifts, key=lambda gift: gift.ratio)
    
    def moyenne_points(self,map:Map,santa):
        list_scale=map.split_in_scale(santa.taille_map//10)
        list_moyenne=[]
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
        for moyenne in list_moyenne:
            somme_moyenne=somme_moyenne+moyenne

        if(len(list_moyenne)==0):
            return None
        return int(somme_moyenne/len(list_moyenne))+santa.taille_map//(santa.taille_map//diviseur(santa.taille_map))

    def clusterisation(self,distance_moyenne):
        list_cluster=[]
        list_gift_restant=self.gifts
        for gift_1 in self.gifts:
            list_courante=[]
            for list_c in list_cluster:
                if gift_1 in list_c:
                    list_courante=list_c
                    list_cluster.remove(list_c)
                    break;
            for gift_2 in list_gift_restant:
                if(gift_2 not in list_courante):
                    if (gift_2.x in range(gift_1.x-distance_moyenne,gift_1.x+distance_moyenne) and gift_2.y in range(gift_1.y-distance_moyenne,gift_1.y+distance_moyenne)):
                        list_courante.append(gift_2)
            list_cluster.append(list_courante)
            list_gift_restant.remove(gift_1)
        list_cluster_temp=list_cluster
        for list_c1 in list_cluster:
            for list_c2 in list_cluster:
                if (list_c1[0] in list_c2 and list_c1!=list_c2):
                    list_cluster_temp.remove(list_c2)
        list_cluster=list_cluster_temp
        self.cluster=list_cluster
        return list_cluster

    def calcul_score_total_cluster(self):
        list_score=[]
        for cluster in self.cluster:
            somme_score_cluster=0
            for gift in cluster:
                somme_score_cluster=somme_score_cluster+gift.score
            list_score.append(somme_score_cluster)
        return list_score