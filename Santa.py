from utils import get_distance
from Gift import Gift
from Game import Game
import matplotlib.pyplot as plt
import matplotlib.image as img
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
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
        self.nb_float = 0
        self.coordonnée = []
        self.deposé = []

        # mise en place de la fenetre d'affichage
        self.fig, self.ax = plt.subplots()
        min_max_x = []
        min_max_y = []
        for gift in self.game.gifts:
            min_max_x.append(gift.x)
            min_max_y.append(gift.y)
        x = [min(min_max_x) - self.game.range, max(min_max_x) + self.game.range]
        y = [min(min_max_y) - self.game.range, max(min_max_y) + self.game.range]
        plt.xlim(x[0], x[1])
        plt.ylim(y[0], y[1])
        self.ax.set_aspect(1)

    def float(self):
        if self.vx == 0 and self.vy == 0:
            return
        self.coordonnée.append((self.x, self.y, self.vx, self.vy))
        self.x += self.vx
        self.y += self.vy
        self.time += 1
        self.nb_float += 1

    def accelerate(self, direction: str, value: int):
        if self.nb_carrots == 0:
            raise Exception('PLUS DE CARROTES !!!')
        speed = self.max_speed()
        if abs(value) > speed:
            raise Exception('Changement de vitesse trop importante')
        if direction == 'vertical':
            self.vy += value
            if value > 0:
                self.add_output(f'AccUp {value}')
            else:
                self.add_output(f'AccDown {-value}')
        else:
            self.vx += value
            if value > 0:
                self.add_output(f'AccRight {value}')
            else:
                self.add_output(f'AccLeft {-value}')
        self.nb_carrots -= 1
        self.weight -= 1
        self.float()

    def load_carrot(self, nb: int):
        if get_distance(self.x, self.y, 0, 0) > self.game.range:
            raise Exception('Distance trop grande pour le ramassage de carrotes')
        self.nb_carrots += nb
        self.weight += nb
        self.add_output(f'LoadCarrots {nb}')

    def load_gift(self, gift: Gift):
        if get_distance(self.x, self.y, 0, 0) > self.game.range:
            raise Exception('Distance trop grande pour le ramassage de cadeaux')
        self.gifts.append(gift)
        self.weight += gift.weight
        self.add_output(f'LoadGift {gift.name}')

    def deliver(self, gift: Gift):
        self.deposé.append((gift.x, gift.y))
        if get_distance(self.x, self.y, gift.x, gift.y) > self.game.range:
            raise Exception(f'Distance trop grande pour déposer de cadeau {gift.name}')
        self.score += gift.score
        self.weight -= gift.weight

        self.gifts.remove(gift)
        self.add_output(f'DeliverGift {gift.name}')

    def max_speed(self):
        for k, v in self.game.acceleration_ranges.items():
            if k >= self.weight:
                return v
        return 0

    def add_output(self, string: str):
        if self.nb_float:
            self.output += f"\nFloat {self.nb_float}"
            self.nb_float = 0
        self.output += f"\n{string}"

    def print(self):
        self.add_output('')
        size = len(self.output.split('\n')) - 2
        final = str(size) + self.output
        with open('output.txt', 'w') as outFile:
            outFile.write(final)
        return final

    def affichage(self):
        #mise en place de la fenetre d'affichage


        #affichage des cadeaux
        for gift in self.game.gifts:
            x = gift.x
            y = gift.y
            if self.game.range==0 :
                circle = plt.Circle((x, y), 1, color='b', fill=False)
            else:
                circle = plt.Circle((x, y), self.game.range, color='b',fill=False)
            self.ax.add_artist(circle)

        #mise en place du pere noel et de sa taille (le z)
        z=0.05
        hamster = img.imread('hamster.png')
        imagebox = OffsetImage(hamster, zoom=z)
        ab = AnnotationBbox(imagebox, (0, 0))
        self.ax.add_artist(ab)
        plt.grid(linestyle='--')
        #affichage des vecteurs
        for elem in self.coordonnée:
            plt.quiver(elem[0], elem[1], elem[2], elem[3], angles='xy', scale_units='xy', scale=0.5, color="r")

        #affichage des cadeau pris
        for elem in self.deposé :
            circle = plt.Circle((elem[0], elem[1]), self.game.range, color='r', fill=False)
            self.ax.add_artist(circle)



