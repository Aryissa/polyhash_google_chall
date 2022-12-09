from utils import get_distance
from Gift import Gift
from Game import Game
from tkinter import *


class Santa:
    def __init__(self, game: Game):
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.nb_carrots = 0
        self.weight = 0
        self.game = game
        self.output = ''
        self.gifts = []
        self.score = 0
        self.time = 0

    def float(self):
        self.x += self.vx
        self.y += self.vy
        self.time += 1
        self.output += '\nFloat 1'

    def accelerate(self, direction: str, value: int):
        if self.nb_carrots == 0:
            raise Exception('PLUS DE CARROTES !!!')
        speed = self.max_speed()
        if abs(value) > speed:
            raise Exception('Changement de vitesse trop importante')
        if direction == 'vertical':
            self.vy += value
            if value > 0:
                self.output += f'\nAccRight {value}'
            else:
                self.output += f'\nAccLeft {value}'
            if self.vy > speed:
                self.vy = speed
        else:
            self.vx += value
            if value > 0:
                self.output += f'\nAccUp {value}'
            else:
                self.output += f'\nAccDown {value}'
            if self.vx > speed:
                self.vx = speed
        self.nb_carrots -= 1
        self.weight -= 1
        self.float()

    def load_carrot(self, nb: int):
        if get_distance(self.x, self.y, 0, 0) > self.game.range:
            raise Exception('Distance trop grande pour le ramassage de carrotes')
        self.nb_carrots += nb
        self.weight += nb
        self.output += f'\nLoadCarrots {nb}'

    def load_gift(self, gift: Gift):
        if get_distance(self.x, self.y, 0, 0) > self.game.range:
            raise Exception('Distance trop grande pour le ramassage de cadeaux')
        self.gifts.append(gift)
        self.weight += gift.weight
        self.output += f'\nLoadGift {gift.name}'

    def deliver(self, gift: Gift):
        if get_distance(self.x, self.y, gift.x, gift.y) > self.game.range:
            raise Exception(f'Distance trop grande pour déposer de cadeau {gift.name}')
        self.score += gift.score
        self.weight -= gift.weight
        self.gifts.remove(gift)
        self.output += f'\nDeliverGift {gift.name}'

    def max_speed(self):
        for k, v in self.game.acceleration_ranges.items():
            if k > self.weight:
                return v
        return 0

    def print(self):
        size = len(self.output.split('\n')) - 1
        return str(size) + self.output


    def affichage(self):

        window = Tk()

        min_max_x = []
        min_max_y = []

        for gift in self.game.gifts:
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

        for gift in self.game.gifts:
            x = gift.x
            x = (x + abs(min_x)) * ratio_x
            y = gift.y
            y = (y + abs(min_y)) * ratio_y
            w.create_oval(x - (self.game.range / 2) * ratio_x, y - (self.game.range / 2) * ratio_y,
                          x + (self.game.range / 2) * ratio_x, y + (self.game.range / 2) * ratio_y, fill="red")

        x = [(0 + abs(min_y)) * ratio_x]
        y = [(0 + abs(min_y)) * ratio_y]
        x.append((self.x + abs(min_x)) * ratio_x)
        y.append((self.y + abs(min_y)) * ratio_y)

        w.create_line(x[0], y[0], x[1], y[1], fill="blue")
        del (x[0])
        del (y[0])

        mainloop()
