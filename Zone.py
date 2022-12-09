from Map import Map
from Gift import Gift
from utils import get_distance

class Zone:
    def __init__(self, gifts):
        self.gifts = gifts
        #ratio = 0
        #self.weight = 0
        #for i in gifts:
            #ratio = ratio+ i.ratio
            #self.weight = self.weight+i.weight
        #self.ratio = ratio / len(gifts)
        #self.initial_gift = max(gifts, key=lambda gift: gift.ratio)
    
    def moyenne_points(self,map:Map,diviseur,gifts):
        list_scale=map.split_in_scale(diviseur)
        list_moyenne=[]
        for scale in list_scale:
            list_gift=[]
            for gift in gifts:
                if scale.in_scale(int(gift["x"]),int(gift["y"])):
                    list_gift.append(gift)
            for gift_1 in list_gift:
                somme=0
                if len(list_gift)>1:
                    for gift_2 in list_gift:
                        somme=somme+get_distance(int(gift_1["x"]), int(gift_1["y"]), int(gift_2["x"]), int(gift_2["y"]))
                    list_moyenne.append(somme/(len(list_gift)-1))
        somme_moyenne=0
        for moyenne in list_moyenne:
            somme_moyenne=somme_moyenne+moyenne

        if(len(list_moyenne)==0):
            return None
        return int(somme_moyenne/len(list_moyenne))

    def clusterisation(self,moyenne_points):
        return 0

