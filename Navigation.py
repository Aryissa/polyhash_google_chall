import Game
import Gift
import Santa
from utils import get_distance


class Navigation:

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
