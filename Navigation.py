import Game
import Gift
import Santa
import utils
from utils import get_distance


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

    def gift_here(self, x, y):
        for gift in self.game.gifts:
            if gift.x == x and gift.y == y:
                return True
        return False

    def line(self, x, y):
        lines_x = dict()
        lines_y = dict()
        max_count = 0
        max_vector = (0, 0)
        # from x
        for vector in utils.enumerate_vectors(4):
            count_h = 0
            count_v = 0
            a, b = vector
            for gift in self.game.gifts:
                if a * gift.x <= 0 or b * gift.y <= 0:
                    # Pour ne pas aller dans les 2 sens
                    continue
                # On regarde si le cadeau est sur la droite
                if (a / b) * gift.x + a == gift.y:
                    count_h += gift.score
                if (a / b) * gift.x - a == gift.y:
                    count_v += gift.score
            lines_x[vector] = count_h
            lines_y[vector] = count_v
            if count_h > max_count:
                max_count = count_h
                max_vector = vector
            if count_v > max_count:
                max_count = count_v
                max_vector = vector
        return max_vector, max_count
