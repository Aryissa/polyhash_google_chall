from Map import Map
from Gift import Gift
from utils import get_distance

class Zone:
    def __init__(self, gifts:list):
        self.gifts = gifts
        #ratio = 0
        #self.weight = 0
        #for i in gifts:
            #ratio = ratio+ i.ratio
            #self.weight = self.weight+i.weight
        #self.ratio = ratio / len(gifts)
        #self.initial_gift = max(gifts, key=lambda gift: gift.ratio)
    
    def moyenne_points(self,map:Map,diviseur,gifts:list):
        list_scale=map.split_in_scale(diviseur)
        list_moyenne=[]
        for scale in list_scale:
            list_gift=[]
            for gift in gifts:
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
        return int(somme_moyenne/len(list_moyenne))

    def clusterisation(self,distance_moyenne):
        list_cluster=[]
        for gift_1 in self.gifts:
            list_courante=[]
            for list_c in list_cluster:
                if gift_1 in list_c:
                    list_courante=list_c
                    list_cluster.remove(list_c)
                    break;
            for gift_2 in self.gifts:
                if(gift_2 not in list_courante):
                    if (gift_2.x in range(gift_1.x-distance_moyenne,gift_1.x+distance_moyenne) and gift_2.y in range(gift_1.y-distance_moyenne,gift_1.y+distance_moyenne)):
                        list_courante.append(gift_2)
            list_cluster.append(list_courante)
        return list_cluster

