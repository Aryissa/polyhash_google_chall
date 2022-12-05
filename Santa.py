from utils import get_distance
from Gift import Gift
from Game import Game


class Santa:
    def __init__(self, game: Game):
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.nb_carrots = 0
        self.weight = 0
        self.game = game
        # TODO : Incrémenter le output avec les actions
        self.output = ''
        self.gifts = []
        self.score = 0

    def float(self):
        self.x += self.vx
        self.y += self.vy

    def accelerate(self, direction: str, value: int):
        if direction == 'vertical':
            self.vy += value
            # TODO : ne pas dépasser la vitesse max (accel_range du jeu)
        else:
            self.vx += value
            # TODO : ne pas dépasser la vitesse max (accel_range du jeu)
        self.nb_carrots -= 1
        self.weight -= 1

    def load_carrot(self, nb: int):
        if get_distance(self.x, self.y, 0, 0) > self.game.range:
            raise Exception('Distance trop grande pour le ramassage de carrotes')
        self.nb_carrots += nb
        self.weight += nb

    def load_gift(self, gift: Gift):
        if get_distance(self.x, self.y, 0, 0) > self.game.range:
            raise Exception('Distance trop grande pour le ramassage de cadeaux')
        self.gifts.append(gift)
        self.weight += gift.weight

    def deliver(self, gift: Gift):
        if get_distance(self.x, self.y, gift.x, gift.y) > self.game.range:
            raise Exception(f'Distance trop grande pour déposer de cadeau {gift.name}')
        self.score += gift.score
        self.weight -= gift.weight
        self.gifts.remove(gift)

