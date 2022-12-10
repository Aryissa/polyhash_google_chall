from utils import get_distance
from Gift import Gift
from Game import Game
import matplotlib.pyplot as plt
import matplotlib.image as img
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
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

    def float(self):
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
                self.add_output(f'AccRight {value}')
            else:
                self.add_output(f'AccLeft {value}')
            if self.vy > speed:
                self.vy = speed
        else:
            self.vx += value
            if value > 0:
                self.add_output(f'AccUp {value}')
            else:
                self.add_output(f'AccDown {value}')
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
        self.add_output(f'LoadCarrots {nb}')

    def load_gift(self, gift: Gift):
        if get_distance(self.x, self.y, 0, 0) > self.game.range:
            raise Exception('Distance trop grande pour le ramassage de cadeaux')
        self.gifts.append(gift)
        self.weight += gift.weight
        self.add_output(f'LoadGift {gift.name}')

    def deliver(self, gift: Gift):
        if get_distance(self.x, self.y, gift.x, gift.y) > self.game.range:
            raise Exception(f'Distance trop grande pour déposer de cadeau {gift.name}')
        self.score += gift.score
        self.weight -= gift.weight
        self.gifts.remove(gift)
        self.add_output(f'DeliverGift {gift.name}')

    def max_speed(self):
        for k, v in self.game.acceleration_ranges.items():
            if k > self.weight:
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
        fig, ax = plt.subplots()
        min_max_x = []
        min_max_y = []

        for gift in self.game.gifts:
            min_max_x.append(gift.x)
            min_max_y.append(gift.y)

        x = [min(min_max_x) - self.game.range, max(min_max_x) + self.game.range]
        y = [min(min_max_y) - self.game.range, max(min_max_y) + self.game.range]

        plt.xlim(x[0], x[1])
        plt.ylim(y[0], y[1])
        ax.set_aspect(1)
        if (x[0] > y[0]):
            z: int = x[0] / (y[0]*10)
        else:
            z: int = y[0] / (x[0]*10)
        if(z<0.05):
            z=0.05
        print(z)
        for gift in self.game.gifts:
            x = gift.x
            y = gift.y
            circle = plt.Circle((x, y), self.game.range, color='r',fill=False)
            ax.add_artist(circle)
        hamster = img.imread('hamster.png')


        imagebox = OffsetImage(hamster, zoom=z)
        ab = AnnotationBbox(imagebox, (0, 0))
        ax.add_artist(ab)
        plt.grid(linestyle='--')
        plt.show()