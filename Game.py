from Gift import Gift
from tkinter import *

class Game:
    def __init__(self, challenge):
        self.max_time = int(challenge['time'])
        self.current_time = 0
        self.range = int(challenge['delivery_distance'])
        self.nb_acceleration_ranges = challenge["acceleration_ranges"]
        self.nb_gifts = int(challenge["nb_gifts"])
        self.gifts = []
        for gift in challenge["gifts_list"]:
            self.gifts.append(Gift(
                gift['name'],
                int(gift['weight']),
                int(gift['x']),
                int(gift['y']),
                int(gift['score']),
                float(gift['ratio'])
            ))
        self.acceleration_ranges = dict()
        for r in challenge['accelerations']:
            self.acceleration_ranges[int(r['weight_interval_to'])] = int(r['max_acceleration'])

    def affichage(self):
        window = Tk()

        min_max_x = []
        min_max_y = []

        for gift in self.gifts:
            min_max_x.append(gift.x)
            min_max_y.append(gift.y)

        min_x = min(min_max_x)
        max_x = max(min_max_x)
        min_y = min(min_max_y)
        max_y = max(min_max_y)

        fenetre_x = abs(max_x) + abs(min_x)
        fenetre_y = abs(max_y) + abs(min_y)

        largeur = 500
        longueur = 500

        w = Canvas(window, width=largeur + 10, height=longueur + 10)

        ratio_x = largeur / fenetre_x
        ratio_y = longueur / fenetre_y

        w.pack()

        i = 0
        for gift in self.gifts:
            x = gift.x
            x = (x + abs(min_x)) * ratio_x
            y = gift.y
            y = (y + abs(min_y)) * ratio_y
            i += 1
            w.create_oval(x - (self.range / 2) * ratio_x, y - (self.range / 2) * ratio_y,
                          x + (self.range / 2) * ratio_x, y + (self.range / 2) * ratio_y, fill="red")
        mainloop()
