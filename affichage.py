from parser_challenge import parse_challenge as pc
from parser_challenge import challenge
from pprint import pprint
from tkinter import *

window = Tk()

pc("input/d_decorated_houses.in.txt")
liste = challenge["gifts_list"]


min_max_x=[]
min_max_y=[]

for i in range(0,len(liste)):
    min_max_x.append(int(liste[i]["x"]))
    min_max_y.append(int(liste[i]["y"]))

dist = challenge["delivery_distance"]
print(dist)
min_x=min(min_max_x)
max_x=max(min_max_x)
min_y=min(min_max_y)
max_y=max(min_max_y)


fenetre_x=abs(int(max_x))+abs(int(min_x))
fenetre_y=abs(int(max_y))+abs(int(min_y))

largeur = 500
longueur = 500

w = Canvas(window, width=largeur+10, height=longueur+10)

ratio_x = largeur/fenetre_x
ratio_y = longueur/fenetre_y
#print(int(min_x)*ratio_x)

w.pack()

def affichage():
    global min_x
    global min_y
    i = 0
    while(i!=len(liste)):
        x=liste[i]["x"]
        x=(int(x)+abs(int(min_x)))*ratio_x
        y=liste[i]["y"]
        y=(int(y)+abs(int(min_y)))*ratio_y
        i+=1
        w.create_oval(int(x)-(int(dist)/2)*ratio_x, int(y)-(int(dist)/2)*ratio_y, int(x)+(int(dist)/2)*ratio_x, int(y)+(int(dist)/2)*ratio_y, fill="red")



    


affichage()
mainloop()

