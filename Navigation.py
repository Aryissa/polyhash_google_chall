import Game
import Gift
import Santa
import utils
from utils import get_distance


def gift_here(x, y, gifts):
    for gift in gifts:
        if gift.x == x and gift.y == y:
            return True
    return False


class Navigation:

    def __init__(self, game, santa):
        self.game = game
        self.santa = santa

    def go_point(self, santa: Santa, x, y):
        while santa.x != x or santa.y != y:
            # accélération en abscisse de santa trop élevé, il va dépasser
            # le cadeau dans 2 tours, et y aussi, donc réduire 1 tour avant
            if santa.x + santa.max_speed()*2 > x and santa.y + santa.max_speed()*2 > y:
                santa.accelerate("horizontal", (-santa.vx+x-santa.x)/2)
                santa.accelerate("vertical", -santa.vy+y-santa.y)
            else:
                if santa.x + santa.max_speed() > x:  # accélération en abscisse de santa trop élevé, il va dépasser le cadeau
                    santa.accelerate("horizontal", -santa.vx+x-santa.x)
                    if santa.x == x:
                        santa.accelerate("horizontal", -santa.vx)
                elif santa.x < x and santa.vx == 0:  # abscisse de santa < abscisse point et santa n'avance pas en x
                    santa.accelerate("horizontal", santa.max_speed())
                if santa.y + santa.max_speed() > y:  # accélération en ordonné de santa trop élevé, il va dépasser le cadeau
                    print("test")
                    santa.accelerate("vertical", -santa.vy+y-santa.y)
                    if santa.y == y:
                        santa.accelerate("vertical", -santa.vy)
                elif santa.y < y and santa.vy == 0:  # ordonné de santa < ordonné point et santa n'avance pas en y
                    santa.accelerate("vertical", santa.max_speed())
            if (santa.vx != 0 or santa.vy != 0) and (santa.x != x or santa.y != y):
                santa.float()

    def go(self, x, y):
        dx = abs(self.santa.x - x)
        dy = abs(self.santa.y - y)

    def line(self, x, y):
        lines_x = dict()
        lines_y = dict()
        for vector in utils.enumerate_vectors(4):
            h = []
            v = []
            a, b = vector
            for gift in self.game.gifts:
                if a * gift.x <= 0 or b * gift.y <= 0:
                    # Pour ne pas aller dans les 2 sens
                    continue
                # On regarde si le cadeau est sur la droite
                if gift.x % a == 0 and x + (b / a) * gift.x + b == y + gift.y:
                    v.append(gift)
                if gift.x % a == 0 and x + (b / a) * gift.x - b == y + gift.y:
                    h.append(gift)
            reverse = False
            if a < 0:
                reverse = True
            h = sorted(h, key=lambda g: g.x, reverse=reverse)
            h = sorted(h, key=lambda g: g.x, reverse=reverse)
            lines_x[vector] = h
            lines_y[vector] = v

        return lines_x, lines_y

    def lines_actions(self, x, y):
        v_x, v_y = self.line(x, y)
        actions = []
        for vector, gifts in v_x.items():
            i = 0
            weight = 5
            action = dict()
            action['vector'] = vector
            action['gifts'] = []
            action['score'] = 0
            action['time'] = 1
            while len(gifts) != len(action['gifts']):
                if gift_here(x + vector[0] * (i + 1), y + vector[1] * i, gifts):
                    gift = gifts[len(action['gifts'])]
                    weight += gift.weight
                    if self.max_speed(weight) < vector[0] or self.max_speed(weight) < vector[1]:
                        break
                    action['gifts'].append(gift)
                    action['score'] += gift.score
                action['time'] += 1
                i += 1
            action['time'] = action['time'] * 2 + 4
            actions.append(action)
        return max(actions, key=lambda a: a['score'] / a['time'])

    def lines_navigate_x(self, action):
        y_depart = self.santa.y
        a, b = action['vector']
        self.santa.load_carrot(7)
        for g in action['gifts']:
            self.game.gifts.remove(g)
            self.santa.load_gift(g)
        self.santa.accelerate('horizontal', a)
        if action['time'] == 1:
            self.santa.deliver(self.santa.gifts[0])
            self.santa.accelerate('horizontal', -a)
            self.santa.accelerate('horizontal', -a)
            self.santa.accelerate('horizontal', a)
            return
        if gift_here(self.santa.x, self.santa.y, self.santa.gifts):
            self.santa.deliver(self.santa.gifts[0])
        self.santa.accelerate('vertical', b)
        while len(self.santa.gifts) != 0:
            if gift_here(self.santa.x, self.santa.y, self.santa.gifts):
                self.santa.deliver(self.santa.gifts[0])
            self.santa.float()
        self.santa.accelerate('horizontal', -a)
        self.santa.accelerate('vertical', -b)
        self.santa.accelerate('vertical', -b)
        self.santa.accelerate('horizontal', -a)
        while self.santa.y != y_depart:
            self.santa.float()
        self.santa.accelerate('vertical', b)
        self.santa.load_carrot(1)
        self.santa.accelerate('horizontal', a)



    def max_speed(self, weight):
        for k, v in self.game.acceleration_ranges.items():
            if k > weight:
                return v
        return 0
