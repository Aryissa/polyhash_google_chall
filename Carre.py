from Gift import Gift

class Carre:
    def __init__(self,point_origine,point_final):
        self.point_origine=point_origine
        self.point_final=point_final
    
    def in_scale(self,x_gift,y_gift):
        x_origine,y_origine=self.point_origine
        x_final,y_final=self.point_final
        if ((x_origine<=int(x_gift) and x_final>=int(x_gift)) and (y_origine>=int(y_gift) and y_final<=int(y_gift))):
            return True
        return False
