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
    min_max_x.append(liste[i]["x"])
    min_max_y.append(liste[i]["y"])

min_x=min(min_max_x)
max_x=max(min_max_x)
min_y=min(min_max_y)
max_y=max(min_max_y)

fenetre_x=abs(int(max_x))+abs(int(min_x))+10
fenetre_y=abs(int(max_y))+abs(int(min_y))+10

w = Canvas(window, width=fenetre_x, height=fenetre_y)

w.pack()

def affichage():
    global min_x
    global min_y
    i=0
    while(i!=len(liste)):
        x=liste[i]["x"]
        x=int(x)+abs(int(min_x))
        print("x ",i," : ",x)
        y=liste[i]["y"]
        y=int(y)+abs(int(min_y))
        print("y ",i," : ",y)
        i+=1
        w.create_oval(x, y, (int(x)+10), int(y)+10, fill="red")
    else : 
        pass


affichage()
mainloop()

