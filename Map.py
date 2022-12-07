from parser import parse_challenge
import Gift

class Map:
    def __init__(self,gifts:Gift):
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
    
    def in_map(self,x,y):
        if (x<self.left or x>self.right or y>self.top or y<self.bot):
            return False
        return True
    
    def split_in_scale(self,vmax,gifts):
        list_map=[]
        point_origine_map=(self.left,self.top)
        for i in range(vmax):
            print(i)



        

