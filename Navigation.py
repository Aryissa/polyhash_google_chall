import Game
import Gift
import Santa
from utils import get_distance_x_or_y, enumerate_vectors


def gift_here(x, y, gifts):
    for gift in gifts:
        if gift.x == x and gift.y == y:
            return True
    return False


class Navigation:

    def __init__(self, santa: Santa, game: Game):
        self.santa = santa
        self.game = game

    def go_point(self, x, y):
        # Quand le point est proche de la position de départ
        if get_distance_x_or_y(self.santa.x, x) <= self.santa.max_speed() and get_distance_x_or_y(self.santa.y, y) <= self.santa.max_speed():
            # Pour x
            # Vérifie si la vitesse actuelle n'est pas = à la vitesse max
            if self.santa.vx != get_distance_x_or_y(self.santa.x, x):
                # Vérifie si la vitesse est du bon signe, sinon il faut passer par zéro
                if x > 0:
                    if self.santa.vx < 0:
                        self.set_vx_to_zero(x)
                else:
                    if self.santa.vx > 0:
                        self.set_vx_to_zero(x)
            # Se rend sur le point quand il est positif par rapport à santa
            if x > self.santa.x:
                self.santa.accelerate("horizontal", -self.santa.vx + get_distance_x_or_y(self.santa.x, x))
            # Se rend sur le point quand il est négatif par rapport à santa
            else:
                self.santa.accelerate("horizontal", -self.santa.vx - get_distance_x_or_y(self.santa.x, x))
            self.set_vx_to_zero(x)
            # Pour y
            # Vérifie si la vitesse actuelle n'est pas = à la vitesse max
            if self.santa.vy != get_distance_x_or_y(self.santa.y, y):
                # Vérifie si la vitesse est du bon signe, sinon il faut passer par zéro
                if y > 0:
                    if self.santa.vy < 0:
                        self.set_vy_to_zero(y)
                else:
                    if self.santa.vy > 0:
                        self.set_vy_to_zero(y)
            # Se rend sur le point quand il est positif par rapport à santa
            if y > self.santa.y:
                self.santa.accelerate("vertical", -self.santa.vy + get_distance_x_or_y(self.santa.y, y))
            # Se rend sur le point quand il est négatif par rapport à santa
            else:
                self.santa.accelerate("vertical", -self.santa.vy - get_distance_x_or_y(self.santa.y, y))
        # Quand le point est loin de la coordonée x de départ, vitesse max en x
        if get_distance_x_or_y(self.santa.x, x) >= self.santa.max_speed():
            # Coordonnée positive par rapport à santa
            if x > self.santa.x:
                # Vérifier si y est proche
                if get_distance_x_or_y(self.santa.y, y) < self.santa.max_speed():
                    self.y_is_close(y)
                    self.set_vy_to_zero(y)
                # Vérifie si x s'est rapproché suffisamment avec les deux float de la vérification précédente
                if get_distance_x_or_y(self.santa.x, x) <= self.santa.max_speed():
                    self.x_is_close(x)
                    self.set_vx_to_zero(x)
                # Vérifie si la vitesse actuelle n'est pas = à la vitesse max et si x et y ne sont pas égaux à santa
                if self.santa.vx != self.santa.max_speed() and (x != self.santa.x or y != self.santa.y):
                    # Vérifie si la vitesse est déjà positive, sinon il faut passer par zéro
                    if self.santa.vx < 0:
                        self.set_vx_to_zero(x)
                    self.santa.accelerate("horizontal", -self.santa.vx + self.santa.max_speed())
            # Coordonnée négative par rapport à santa
            else:
                # Vérifier si y est proche
                if get_distance_x_or_y(self.santa.y, y) <= self.santa.max_speed():
                    self.y_is_close(y)
                    self.set_vy_to_zero(y)
                # Vérifie si x s'est rapproché suffisamment avec les deux float de la vérification précédente
                if get_distance_x_or_y(self.santa.x, x) <= self.santa.max_speed():
                    self.x_is_close(x)
                    self.set_vx_to_zero(x)
                # Vérifie si la vitesse actuelle n'est pas = à la vitesse max et si x et y ne sont pas égaux à santa
                if self.santa.vx != -self.santa.max_speed() and (x != self.santa.x or y != self.santa.y):
                    # Vérifie si la vitesse est déjà négative, sinon il faut passer par zéro
                    if self.santa.vx > 0:
                        self.set_vx_to_zero(x)
                    self.santa.accelerate("horizontal", -self.santa.vx - self.santa.max_speed())
        # Quand le point est loin de la coordonée y de départ, vitesse max en y
        if get_distance_x_or_y(self.santa.y, y) >= self.santa.max_speed():
            # Coordonnée positive par rapport à santa
            if y > self.santa.y:
                # Vérifier si x est proche
                if get_distance_x_or_y(self.santa.x, x) <= self.santa.max_speed():
                    self.x_is_close(x)
                    self.set_vx_to_zero(x)
                # Vérifie si y s'est rapproché suffisamment avec les deux float de la vérification précédente
                if get_distance_x_or_y(self.santa.y, y) < self.santa.max_speed():
                    self.y_is_close(y)
                    self.set_vy_to_zero(y)
                # Vérifie si la vitesse actuelle n'est pas = à la vitesse max et si x et y ne sont pas égaux à santa
                if self.santa.vy != self.santa.max_speed() and (x != self.santa.x or y != self.santa.y):
                    # Vérifie si la vitesse est déjà positive, sinon il faut passer par zéro
                    if self.santa.vy < 0:
                        self.set_vy_to_zero(y)
                    self.santa.accelerate("vertical", -self.santa.vy + self.santa.max_speed())
            # Coordonnée négative par rapport à santa
            else:
                # Vérifier si x est proche
                if get_distance_x_or_y(self.santa.x, x) <= self.santa.max_speed():
                    self.x_is_close(x)
                    self.set_vx_to_zero(x)
                # Vérifie si y s'est rapproché suffisamment avec les deux float de la vérification précédente
                if get_distance_x_or_y(self.santa.y, y) < self.santa.max_speed():
                    self.y_is_close(y)
                    self.set_vy_to_zero(y)
                # Vérifie si la vitesse actuelle n'est pas = à la vitesse max et si x et y ne sont pas égaux à santa
                if self.santa.vy != -self.santa.max_speed() and (x != self.santa.x or y != self.santa.y):
                    # Vérifie si la vitesse est déjà négative, sinon il faut passer par zéro
                    if self.santa.vy > 0:
                        self.set_vy_to_zero(y)
                    self.santa.accelerate("vertical", -self.santa.vy - self.santa.max_speed())
        # Tant qu'on n'est pas arrivé au point voulu
        while x != self.santa.x or y != self.santa.y:
            # Vérifie si x et y sont tous les deux proches du point voulu
            if get_distance_x_or_y(self.santa.x, x) <= self.santa.max_speed()*2 and get_distance_x_or_y(self.santa.y, y) <= self.santa.max_speed()*2 and x != self.santa.x and y != self.santa.y:
                # Au moins une des deux distances est impaire :
                if get_distance_x_or_y(self.santa.x, x) % 2 != 0 or get_distance_x_or_y(self.santa.y, y) % 2 != 0:
                    self.set_vx_to_zero(x)
                    self.y_is_close(y)
                    self.set_vy_to_zero(y)
                    self.x_is_close(x)
                else:
                    if self.santa.vx > 0:
                        self.santa.accelerate("horizontal", -self.santa.vx + get_distance_x_or_y(self.santa.x, x) // 2)
                    else:
                        self.santa.accelerate("horizontal", -self.santa.vx - get_distance_x_or_y(self.santa.x, x) // 2)
                    if get_distance_x_or_y(self.santa.y, y) <= self.santa.max_speed():
                        self.y_is_close(y)
            # Vérifie si x est proche du point voulu
            if get_distance_x_or_y(self.santa.x, x) <= self.santa.max_speed() and x != self.santa.x:
                self.x_is_close(x)
                if y != self.santa.y:
                    self.set_vx_to_zero(x)
            # Vérifie si y est proche du point voulu
            if get_distance_x_or_y(self.santa.y, y) <= self.santa.max_speed() and y != self.santa.y:
                self.y_is_close(y)
                if x != self.santa.x:
                    self.set_vy_to_zero(y)
            if x != self.santa.x or y != self.santa.y:
                self.santa.float()

    def y_is_close(self, y):
        self.santa.accelerate("vertical", -self.santa.vy + y - self.santa.y)

    def x_is_close(self, x):
        self.santa.accelerate("horizontal", -self.santa.vx + x - self.santa.x)

    def set_vx_to_zero(self, x):
        self.santa.accelerate("horizontal", -self.santa.vx)

    def set_vy_to_zero(self, y):
        self.santa.accelerate("vertical", -self.santa.vy)


    def line(self, x, y):
        lines_x = dict()
        lines_y = dict()
        for vector in enumerate_vectors(4):
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
