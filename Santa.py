from utils import get_distance
from Gift import Gift
from Game import Game
import matplotlib.pyplot as plt
import matplotlib.image as img
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from Zone import Zone
import random


class Santa:
    """
    Classe père Noël
    Comprend les différentes actions effectuées par le père Noël
    """

    def __init__(self, game: Game, zone: Zone = None):
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.nb_carrots = 0
        self.weight = 0
        self.game = game
        self.zone = zone
        self.output = ''
        self.gifts = []
        self.score = 0
        self.time = 0
        self.nb_float = 0
        self.coordinates = []
        self.delivered = []

        # mise en place de la fenêtre d'affichage
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
        self.taille_map = abs(x[0]) + abs(x[1])

    """
    Modifie les attributs du père Noël à chaque float
    """
    def float(self):
        self.coordinates.append((self.x, self.y, self.vx, self.vy))
        self.x += self.vx
        self.y += self.vy
        self.time += 1
        self.nb_float += 1

    """
    Permet au père Noël d'accélérer
    """
    def accelerate(self, direction: str, value: int):
        if self.nb_carrots == 0:
            raise Exception('PLUS DE CARROTES !!!')
        speed = self.max_acceleration()
        if abs(value) > speed:
            raise Exception(
                f'Changement de vitesse trop importante. Changement de vitesse : {value}, max speed : {speed}')
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

    """
    Charge des carottes
    """
    def load_carrot(self, nb: int):
        if get_distance(self.x, self.y, 0, 0) > self.game.range:
            raise Exception(f'Distance trop grande pour le ramassage de carrotes {self.x, self.y}')
        self.nb_carrots += nb
        self.weight += nb
        self.add_output(f'LoadCarrots {nb}')

    """
    Charge les cadeaux
    """
    def load_gift(self, gift: Gift):
        if get_distance(self.x, self.y, 0, 0) > self.game.range:
            raise Exception('Distance trop grande pour le ramassage de cadeaux')
        self.gifts.append(gift)
        self.weight += gift.weight
        self.add_output(f'LoadGift {gift.name}')

    """
    Dépose le cadeau en paramètre
    """
    def deliver(self, gift: Gift):
        self.delivered.append((gift.x, gift.y))
        if get_distance(self.x, self.y, gift.x, gift.y) > self.game.range:
            raise Exception(f'Distance trop grande pour déposer de cadeau {gift.name}')
        self.score += gift.score
        self.weight -= gift.weight

        self.gifts.remove(gift)
        self.add_output(f'DeliverGift {gift.name}')

    """
    Retourne accélération maximum
    """
    def max_acceleration(self):
        for k, v in self.game.acceleration_ranges.items():
            if k >= self.weight:
                return v
        return 0

    """
    Ajoute chaque action au print final
    """
    def add_output(self, string: str):
        if self.nb_float:
            self.output += f"\nFloat {self.nb_float}"
            self.nb_float = 0
        self.output += f"\n{string}"

    """
    Affiche le print final contenant l'ensemble des actions effectuées
    """
    def print(self):
        self.add_output('')
        size = len(self.output.split('\n')) - 2
        final = str(size) + self.output
        with open('output.txt', 'w') as outFile:
            outFile.write(final)
        return final

    """
    Initialise l'affichage des cadeaux
    """
    def affichage_init(self):
        for gift in self.game.gifts:
            x = gift.x
            y = gift.y
            if self.game.range == 0:
                circle = plt.Circle((x, y), 1, color='b', fill=False)
            else:
                circle = plt.Circle((x, y), self.game.range, color='b', fill=False)
            self.ax.add_artist(circle)

    """
    Affiche les cadeaux, le père Noël, les vecteurs et change la couleur d'un cadeau déposés
    """
    def affichage(self):
        # affichage des cadeaux
        self.affichage_init()
        # mise en place du pere noel et de sa taille (le z)
        z = 0.05
        hamster = img.imread('hamster.png')
        imagebox = OffsetImage(hamster, zoom=z)
        ab = AnnotationBbox(imagebox, (0, 0))
        self.ax.add_artist(ab)
        plt.grid(linestyle='--')
        # affichage des vecteurs
        for elem in self.coordinates:
            plt.quiver(elem[0], elem[1], elem[2], elem[3], angles='xy', scale_units='xy', scale=1, color="g",
                       headwidth=0, )

        # affichage des cadeaux déposés
        for elem in self.delivered:
            circle = plt.Circle((elem[0], elem[1]), self.game.range, color='r', fill=False)
            self.ax.add_artist(circle)

    """
    Affiche des clusters
    """
    def affichage_zone(self):
        # récupération des données de zone
        new_cluster = []
        for gift in self.zone.cluster:
            color1 = random.randint(5, 255)
            color2 = random.randint(5, 255)
            for objet in gift:
                x = objet.x
                y = objet.y
                new_cluster.append((x, y))
                if self.game.range == 0:
                    circle = plt.Circle((x, y), 1, color=(1, color1 / 255, color2 / 255), fill=False)
                else:
                    circle = plt.Circle((x, y), self.game.range, color=(1, color1 / 250, 0), fill=False)
                self.ax.add_artist(circle)
