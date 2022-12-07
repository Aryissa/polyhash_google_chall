from parser_challenge import parse_challenge as pc
from parser_challenge import challenge
from pprint import pprint
from tkinter import *

window = Tk()

pc("input/a_an_example.in.txt")
liste = challenge["gifts_list"]
min_max_x=[]
min_max_y=[]

for i in range(0,len(liste)):
    min_max_x.append(int(liste[i]["x"]))
    min_max_y.append(int(liste[i]["y"]))

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

print(ratio_x)
print(ratio_y)

#print(int(min_x)*ratio_x)

w.pack()

def affichage():
    global min_x
    global min_y
    i = 0
    while(i!=len(liste)):
        x=liste[i]["x"]
        print("x : ",x)
        print(ratio_x)
        x=(int(x)+abs(int(min_x)))*ratio_x
        print("x ",i," : ",x)
        y=liste[i]["y"]
        print("y : ",y)
        print(ratio_y)

        y=(int(y)+abs(int(min_y)))*ratio_y
        print("y ",i," : ",y)
        i+=1
        w.create_oval(x, y, int(x)+10, int(y)+10, fill="red")



    


affichage()
mainloop()

