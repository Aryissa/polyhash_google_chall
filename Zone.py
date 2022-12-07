import math
import Map
class Zone:
    def __init__(self, gifts):
        self.gifts = gifts
        ratio = 0
        self.weight = 0
        for i in gifts:
            ratio += i.ratio
            self.weight += i.weight
        self.ratio = ratio / len(gifts)
        self.initial_gift = max(gifts, key=lambda gift: gift.ratio)
    
    def distance_point(xa:int,ya:int,xb:int,yb:int):
        return math.sqrt((abs(xa-xb))**2+(abs(ya-yb))**2)

    
