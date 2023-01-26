import Gift
from Carre import Carre


"""
Class Map
Permet la définission d'une Map réduite 
"""
class Map:
    def __init__(self,gifts:list):
        self.top,self.bot,self.left,self.right,self.l_x,self.l_y=0,0,0,0,0,0
        for gift in gifts:
            x=gift.x
            y=gift.y
            if(self.top==0 and self.bot==0 and self.left==0 and self.right==0):
                self.top,self.bot=y,y
                self.left,self.right=x,x 
            if (self.left>x):
                self.left=x
            if (self.right<x):
                self.right=x
            if (self.top<y):
                self.top=y
            if (self.bot>y):
                self.bot=y
        self.l_x=self.right-self.left
        self.l_y=self.top-self.bot
    

    """
    Permet de dire si un point se situe dans la map
    x: position x du point
    y; position y du point
    """
    def in_map(self,x,y):
        if (x<self.left or x>self.right or y>self.top or y<self.bot):
            return False
        return True
    
    #pas représente en combien tous les combien on créer un carré
    """
    Permet la création d'une liste de Carré qui découpe la Map
    Cette liste représente l'ensemble des sous-map de la Map
    pas: est un int qui définit la taille de chaque carré
    """
    def split_in_scale(self,pas:int):
        list_map=[]
        point_origine_map=(self.left,self.top)
        point_final=(self.left+pas,self.top-pas)
        X=int(self.l_x/pas)
        Y=int(self.l_y/pas)
        for i in range(X*Y*pas):
            list_map.append(Carre(point_origine_map,point_final))
            x_origine,y_origine=point_origine_map
            x_final,y_final=point_final
            
            if(x_final==self.right): #si notre x tombe pile sur le bord alors on repars
                x_origine=self.left
                x_final=x_origine+pas
                if(y_final-pas<self.bot):
                    if y_final==self.bot:
                        #self.print_all(list_map)
                        return list_map
                    else:
                        y_origine=y_final
                        y_final=self.bot
                else:
                    y_origine=y_final
                    y_final=y_final-pas

            elif (x_final+pas>self.right): #si on dépasse de la map
                if (x_final<self.right):
                    x_origine=x_final
                    x_final=self.right
                else:
                    x_origine=self.left
                    x_final=x_origine+pas


            else:
                x_origine=x_final
                x_final=x_final+pas
    
            
            point_final=(x_final,y_final)
            point_origine_map=(x_origine,y_origine)
        #self.print_all(list_map)
        return list_map
    

    """
    permet d'afficher l'ensemble des listes de Carré
    """
    def print_all(self,list):
        print("map: top ", self.top,"map: bot ",self.bot,"map: left ",self.left,"map: right ", self.right )
        for carre in list:
            print("point origine: ",carre.point_origine," point final: ",carre.point_final)



                



        

