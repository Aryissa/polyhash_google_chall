import Game
import Gift
import Santa
from utils import get_distance_x_or_y, enumerate_vectors, gift_here, gifts_in_range


class Navigation:

    def __init__(self, santa: Santa, game: Game):
        self.santa = santa
        self.game = game

    def go_point(self, x, y):
        if x == self.santa.x and self.santa.vx != 0:
            self.set_vx_to_zero()
        if y == self.santa.y and self.santa.vy != 0:
            self.set_vy_to_zero()
        if x > self.santa.x:
            if self.santa.vx < 0:
                self.set_vx_to_zero()
        else:
            if self.santa.vx > 0:
                self.set_vx_to_zero()
        if y > self.santa.y:
            if self.santa.vy < 0:
                self.set_vy_to_zero()
        else:
            if self.santa.vy > 0:
                self.set_vy_to_zero()
        # Quand le point est proche de la position de départ
        if get_distance_x_or_y(self.santa.x, x) <= self.santa.max_speed() and get_distance_x_or_y(self.santa.y, y) <= self.santa.max_speed():
            # Pour x
            # Se rend sur le point quand il est positif par rapport à santa
            if x > self.santa.x:
                self.santa.accelerate("horizontal", -self.santa.vx + get_distance_x_or_y(self.santa.x, x))
            # Se rend sur le point quand il est négatif par rapport à santa
            else:
                self.santa.accelerate("horizontal", -self.santa.vx - get_distance_x_or_y(self.santa.x, x))
            self.set_vx_to_zero()
            # Pour y
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
                if get_distance_x_or_y(self.santa.y, y) <= self.santa.max_speed() and y != self.santa.y:
                    self.y_is_close(y)
                    self.set_vy_to_zero()
                # Vérifie si x s'est rapproché suffisamment avec les deux float de la vérification précédente
                if get_distance_x_or_y(self.santa.x, x) <= self.santa.max_speed() and x != self.santa.x:
                    self.x_is_close(x)
                    self.set_vx_to_zero()
                # Vérifie si la vitesse actuelle n'est pas = à la vitesse max et si x et y ne sont pas égaux à santa
                if self.santa.vx != self.santa.max_speed() and (x != self.santa.x):
                    # Vérifie si la vitesse est déjà positive, sinon il faut passer par zéro
                    if self.santa.vx < 0:
                        self.set_vx_to_zero()
                    self.santa.accelerate("horizontal", -self.santa.vx + self.santa.max_speed())
            # Coordonnée négative par rapport à santa
            else:
                # Vérifier si y est proche
                if get_distance_x_or_y(self.santa.y, y) <= self.santa.max_speed() and y != self.santa.y:
                    self.y_is_close(y)
                    self.set_vy_to_zero()
                # Vérifie si x s'est rapproché suffisamment avec les deux float de la vérification précédente
                if get_distance_x_or_y(self.santa.x, x) <= self.santa.max_speed() and x != self.santa.x:
                    self.x_is_close(x)
                    self.set_vx_to_zero()
                # Vérifie si la vitesse actuelle n'est pas = à la vitesse max et si x et y ne sont pas égaux à santa
                if self.santa.vx != -self.santa.max_speed() and (x != self.santa.x):
                    # Vérifie si la vitesse est déjà négative, sinon il faut passer par zéro
                    if self.santa.vx > 0:
                        self.set_vx_to_zero()
                    self.santa.accelerate("horizontal", -self.santa.vx - self.santa.max_speed())
        # Quand le point est loin de la coordonée y de départ, vitesse max en y
        if get_distance_x_or_y(self.santa.y, y) >= self.santa.max_speed():
            # Coordonnée positive par rapport à santa
            if y > self.santa.y:
                # Vérifier si x est proche
                if get_distance_x_or_y(self.santa.x, x) <= self.santa.max_speed() and x != self.santa.x:
                    self.x_is_close(x)
                    self.set_vx_to_zero()
                # Vérifie si y s'est rapproché suffisamment avec les deux float de la vérification précédente
                if get_distance_x_or_y(self.santa.y, y) < self.santa.max_speed() and y != self.santa.y:
                    self.y_is_close(y)
                    self.set_vy_to_zero()
                # Vérifie si la vitesse actuelle n'est pas = à la vitesse max et si x et y ne sont pas égaux à santa
                if self.santa.vy != self.santa.max_speed() and (y != self.santa.y):
                    # Vérifie si la vitesse est déjà positive, sinon il faut passer par zéro
                    if self.santa.vy < 0:
                        self.set_vy_to_zero()
                    self.santa.accelerate("vertical", -self.santa.vy + self.santa.max_speed())
            # Coordonnée négative par rapport à santa
            else:
                # Vérifier si x est proche
                if get_distance_x_or_y(self.santa.x, x) <= self.santa.max_speed() and x != self.santa.x:
                    self.x_is_close(x)
                    self.set_vx_to_zero()
                # Vérifie si y s'est rapproché suffisamment avec les deux float de la vérification précédente
                if get_distance_x_or_y(self.santa.y, y) < self.santa.max_speed() and y != self.santa.y:
                    self.y_is_close(y)
                    self.set_vy_to_zero()
                # Vérifie si la vitesse actuelle n'est pas = à la vitesse max et si x et y ne sont pas égaux à santa
                if self.santa.vy != -self.santa.max_speed() and (y != self.santa.y):
                    # Vérifie si la vitesse est déjà négative, sinon il faut passer par zéro
                    if self.santa.vy > 0:
                        self.set_vy_to_zero()
                    self.santa.accelerate("vertical", -self.santa.vy - self.santa.max_speed())
        # Tant qu'on n'est pas arrivé au point voulu
        while x != self.santa.x or y != self.santa.y:
            if self.santa.time >= self.game.max_time:
                return False
            # Vérifie si x et y sont tous les deux proches du point voulu
            if get_distance_x_or_y(self.santa.x, x) <= self.santa.max_speed()*2 and get_distance_x_or_y(self.santa.y, y) <= self.santa.max_speed()*2 and x != self.santa.x and y != self.santa.y:
                # Au moins une des deux distances est impaire :
                if get_distance_x_or_y(self.santa.x, x) % 2 != 0 or get_distance_x_or_y(self.santa.y, y) % 2 != 0:
                    if get_distance_x_or_y(self.santa.x, x) < get_distance_x_or_y(self.santa.y, y):
                        self.set_vx_to_zero()
                        self.y_is_close(y)
                        self.set_vy_to_zero()
                        if get_distance_x_or_y(self.santa.x, x) >= self.santa.max_speed():
                            if self.santa.x < x:
                                self.santa.accelerate("horizontal", self.santa.max_speed())
                            if self.santa.x > x:
                                self.santa.accelerate("horizontal", -self.santa.max_speed())
                        if self.santa.x != x:
                            self.x_is_close(x)
                    else: # faire un else if > et un else =
                        self.set_vy_to_zero()
                        self.x_is_close(x)
                        self.set_vx_to_zero()
                        if get_distance_x_or_y(self.santa.y, y) >= self.santa.max_speed():
                            if self.santa.y < y:
                                self.santa.accelerate("vertical", self.santa.max_speed())
                            if self.santa.y > y:
                                self.santa.accelerate("vertical", -self.santa.max_speed())
                        if self.santa.y != y:
                            self.y_is_close(y)
                else:
                    if get_distance_x_or_y(self.santa.x, x) < get_distance_x_or_y(self.santa.y, y):
                        if self.santa.vx > 0:
                            self.santa.accelerate("horizontal", -self.santa.vx + get_distance_x_or_y(self.santa.x, x) // 2)
                        else:
                            self.santa.accelerate("horizontal", -self.santa.vx - get_distance_x_or_y(self.santa.x, x) // 2)
                        if get_distance_x_or_y(self.santa.y, y) <= self.santa.max_speed():
                            self.y_is_close(y)
                    else: # faire un else if > et un else =
                        if self.santa.vy > 0:
                            self.santa.accelerate("vertical", -self.santa.vy + get_distance_x_or_y(self.santa.y, y) // 2)
                        else:
                            self.santa.accelerate("vertical", -self.santa.vy - get_distance_x_or_y(self.santa.y, y) // 2)
                        if get_distance_x_or_y(self.santa.x, x) <= self.santa.max_speed():
                            self.x_is_close(x)
            # Vérifie si x est proche du point voulu
            if get_distance_x_or_y(self.santa.x, x) <= self.santa.max_speed() and x != self.santa.x:
                self.x_is_close(x)
                if y != self.santa.y:
                    self.set_vx_to_zero()
            # Vérifie si y est proche du point voulu
            if get_distance_x_or_y(self.santa.y, y) <= self.santa.max_speed() and y != self.santa.y:
                self.y_is_close(y)
                if x != self.santa.x:
                    self.set_vy_to_zero()
                    if get_distance_x_or_y(self.santa.x, x) <= self.santa.max_speed() and x != self.santa.x:
                        self.x_is_close(x)
            if x != self.santa.x or y != self.santa.y:
                self.santa.float()
        return True

    def y_is_close(self, y):
        if y > self.santa.y:
            if self.santa.vy < 0:
                self.set_vy_to_zero()
        else:
            if self.santa.vy > 0:
                self.set_vy_to_zero()
        self.santa.accelerate("vertical", -self.santa.vy + y - self.santa.y)

    def x_is_close(self, x):
        if x > self.santa.x:
            if self.santa.vx < 0:
                self.set_vx_to_zero()
        else:
            if self.santa.vx > 0:
                self.set_vx_to_zero()
        self.santa.accelerate("horizontal", -self.santa.vx + x - self.santa.x)

    def set_vx_to_zero(self):
        self.santa.accelerate("horizontal", -self.santa.vx)

    def set_vy_to_zero(self):
        self.santa.accelerate("vertical", -self.santa.vy)

    def run_line(self, method=1):
        if method == 0:
            while True:
                action = self.lines_actions(0, 0)
                if self.santa.time + action['time'] > self.game.max_time:
                    break
                self.lines_navigate_x(action)
        if method == 1:
            while True:
                action = self.lines_r_actions(0, 0)
                if self.santa.time + action['time'] > self.game.max_time:
                    break
                self.lines_r_navigate_x(action)
        if method == 2:
            while True:
                actions = self.lines_rs_actions_2(0, 0)

                action = None
                #pprint(actions)
                for a in actions:
                    if self.santa.time + a['time'] <= self.game.max_time:
                        action = a
                        break

                if not action:
                    print("Pas de temps de trajets assez petits")
                    break

                # On regarde si on peut faire un petit trajet juste avant le dernier
                action2 = None
                if self.santa.time + (action['time'] * 2) > self.game.max_time:
                    for a in actions:
                        if self.santa.time + action['time'] + (a['time']*2) <= self.game.max_time:
                            action2 = a
                            break
                if action2:
                    action = action2

                self.lines_rs_navigate_x(action)

                if self.santa.time + action['time'] > self.game.max_time:
                    print(f"Pas assez de temps pour le retour ({action['time']})")
                    break
                self.lines_rs_return_x(action['vector'], action['nb_accel'])

        #if method == 3:
        #    while True:
        #        action1 = self.lines_rs_actions_2(0, 0)
        #        action2 = self.lines_r_actions(0, 0)
        #        if action1['score'] / action1['time'] >= action2['score'] / action2['time']:
        #            if self.santa.time + action1['time'] > self.game.max_time:
        #                break
        #            self.lines_rs_navigate_x(action1)
        #        else:
        #            if self.santa.time + action2['time'] > self.game.max_time:
        #                break
        #            self.lines_r_navigate_x(action2)

    def line(self, x, y, max_speed=4):
        lines_x = dict()
        lines_y = dict()
        for vector in enumerate_vectors(max_speed):
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

    def line_r(self, x, y, max_speed=4):
        lines_x = dict()
        lines_y = dict()
        for vector in enumerate_vectors(max_speed):
            h = []
            v = []
            a, b = vector
            for gift in self.game.gifts:
                if a * gift.x <= 0 or b * gift.y <= 0:
                    # Pour ne pas aller dans les 2 sens
                    continue
                # On regarde si le cadeau est sur la droite
                x_res = x + (b / a) * gift.x + b
                y_res = x + (b / a) * gift.x - b
                if y + gift.y + self.game.range >= x_res >= y + gift.y - self.game.range:
                    v.append(gift)
                if y + gift.y + self.game.range >= y_res >= y + gift.y - self.game.range:
                    h.append(gift)
            h = sorted(h, key=lambda g: g.x, reverse=a < 0)
            v = sorted(v, key=lambda g: g.x, reverse=a < 0)
            lines_x[vector] = h
            lines_y[vector] = v
        return lines_x, lines_y

    def lines_r_actions(self, x, y):
        v_x, v_y = self.line_r(x, y)
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
                available_gifts = gifts_in_range(x + vector[0] * (i + 1), y + vector[1] * i, self.game.range, gifts)
                available_gifts.sort(key=lambda g: g.score)
                end = False
                for gift in available_gifts:
                    if gift in action['gifts']:
                        continue
                    weight += gift.weight
                    if self.max_speed(weight) < abs(vector[0]) or self.max_speed(weight) < abs(vector[1]):
                        end = True
                        break
                    action['gifts'].append(gift)
                    action['score'] += gift.score
                if end:
                    break
                action['time'] += 1

                i += 1
            action['time'] = action['time'] * 2 + 4

            actions.append(action)
        return max(actions, key=lambda a: a['score'] / a['time'])

    def lines_r_navigate_x(self, action):
        y_depart = self.santa.y
        a, b = action['vector']
        #self.santa.load_carrot(7)
        #print(f"nb carrots : {self.santa.nb_carrots}")
        self.santa.load_carrot(7 - self.santa.nb_carrots if 7 >= self.santa.nb_carrots else 0)
        for g in action['gifts']:
            self.game.gifts.remove(g)
            self.santa.load_gift(g)
        self.santa.accelerate('horizontal', a)
        if action['time'] == 1:
            for gift in gifts_in_range(self.santa.x, self.santa.y, self.santa.range, self.santa.gifts):
                self.santa.deliver(gift)
            self.santa.accelerate('horizontal', -a)
            self.santa.accelerate('horizontal', -a)
            self.santa.accelerate('horizontal', a)
            return
        for gift in gifts_in_range(self.santa.x, self.santa.y, self.game.range, self.santa.gifts):
            self.santa.deliver(gift)
        self.santa.accelerate('vertical', b)
        while len(self.santa.gifts) != 0:
            for gift in gifts_in_range(self.santa.x, self.santa.y, self.game.range, self.santa.gifts):
                self.santa.deliver(gift)
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

    def lines_rs_actions(self, x, y):
        max_speed = max(self.game.acceleration_ranges.values())
        v_x, v_y = self.line_r(x, y, max_speed=max_speed)
        actions = []
        for vector, gifts in v_x.items():
            i = 0
            weight = 0
            action = dict()
            action['vector'] = vector
            action['gifts'] = []
            action['score'] = 0
            action['time'] = 1
            nb_carrots = 0
            max_x = max(self.game.gifts, key=lambda g: g.x).x
            min_x = min(self.game.gifts, key=lambda g: g.x).x
            vx = vy = 0
            nx, ny = x, y
            second = True
            while len(gifts) != len(action['gifts']) and min_x < nx < max_x:
                #available_gifts = gifts_in_range(x + vector[0] * (i + 1), y + vector[1] * i, self.game.range, gifts)
                available_gifts = gifts_in_range(nx, ny, self.game.range, gifts)
                available_gifts.sort(key=lambda g: g.score)
                end = False
                for gift in available_gifts:
                    if gift in action['gifts']:
                        continue
                    weight += gift.weight
                    if self.max_speed(weight + nb_carrots) < abs(vector[0]) or self.max_speed(weight + nb_carrots) < abs(vector[1]):
                        end = True
                        weight -= gift.weight
                        break
                    action['gifts'].append(gift)
                    action['score'] += gift.score
                if end:
                    break
                action['time'] += 1
                if i % 2:
                    if vx <= self.game.range:
                        vx += vector[0]
                        nb_carrots += 4
                else:
                    if vy <= self.game.range:
                        vy += vector[1]
                        nb_carrots += + 4
                if second:
                    i += 1
                second = not second
                nx += vx
                ny += vy
            action['time'] = action['time'] * 4
            action['carrots'] = nb_carrots
            while self.max_speed(weight + nb_carrots) < max([abs(vector[0]), abs(vector[1])]):
                weight -= action['gifts'].pop().weight
            #print(vector, weight, + nb_carrots, self.max_speed(weight + nb_carrots), max([abs(vector[0]), abs(vector[1])]))
            actions.append(action)
        return max(actions, key=lambda a: a['score'] / a['time'])

    def find_nb_accel(self, x, y, vector, gifts):
        weight = 0
        last_x = 0
        a, b = vector
        for gift in gifts:
            weight += gift.weight
            if self.max_speed(weight) < max([abs(a), abs(b)]):
                break
            last_x = gift.x
        dx_b = 0
        vx = 0
        counter = 0
        last_x = abs(x - last_x)
        while abs(dx_b) * 2 < last_x:
            counter += 1
            vx += a
            dx_b += vx
        return counter

    def lines_rs_actions_2(self, x, y):
        max_speed = max(self.game.acceleration_ranges.values())
        v_x, v_y = self.line_r(x, y, max_speed=max_speed)
        actions = []
        for vector, gifts in v_x.items():
            action = dict()
            action['vector'] = vector
            action['gifts'] = []
            action['score'] = 0
            action['time'] = 0
            nb_carrots = 0
            weight = 0
            nb_accel = self.find_nb_accel(x, y, vector, gifts) + 1
            action['nb_accel'] = nb_accel
            vx = vy = 0
            nx, ny = x, y
            for m in [1, -1]:
                second = True
                i = 0
                for _ in range(nb_accel):
                    available_gifts = gifts_in_range(nx, ny, self.game.range, gifts)
                    available_gifts.sort(key=lambda g: g.score)
                    end = False
                    for gift in available_gifts:
                        if gift in action['gifts']:
                            continue
                        weight += gift.weight
                        if self.max_speed(weight + nb_carrots) < max([abs(vector[0]), abs(vector[1])]) or self.max_speed(weight + nb_carrots) < abs(vector[1]):
                            end = True
                            weight -= gift.weight
                            break
                        action['gifts'].append(gift)
                        action['score'] += gift.score
                    if end:
                        break
                    if i % 2 == 0:
                        vx += vector[0] * m
                    else:
                        vy += vector[1] * m
                    if second:
                        i += 1
                    second = not second
                    action['time'] += 1
                    nx += vx
                    ny += vy
                    nb_carrots += 2
            action['time'] += action['nb_accel'] * 2  # action['time'] * 2
            action['carrots'] = action['nb_accel'] * 4
            while self.max_speed(weight + action['carrots']) < max([abs(vector[0]), abs(vector[1])]):
                weight -= action['gifts'].pop().weight

            if len(action['gifts']) != 0:
                actions.append(action)
        actions.sort(key=lambda a: a['score'] / a['time'], reverse=True)
        return actions

    def lines_rs_navigate_x(self, action):
        #print('\nNOUVEAU TRAJET')
        #print(action['vector'])
        #print(f"time:{action['time']} nbgifts:{len(action['gifts'])} carrots:{action['carrots']} score:{action['score']}")
        a, b = action['vector']
        self.santa.load_carrot(action['carrots'] - self.santa.nb_carrots if action['carrots'] >= self.santa.nb_carrots else 0)
        for g in action['gifts']:
            self.game.gifts.remove(g)
            self.santa.load_gift(g)
        for m in [1, -1]:
            second = True
            nb = 0
            for _ in range(action['nb_accel']):
                for gift in gifts_in_range(self.santa.x, self.santa.y, self.game.range, self.santa.gifts):
                    self.santa.deliver(gift)
                if nb % 2 == 0:
                    self.santa.accelerate('horizontal', m * a)
                else:
                    self.santa.accelerate('vertical', m * b)
                if second:
                    nb += 1
                second = not second

    def lines_rs_return_x(self, vector, nb_accel):
        a, b = vector
        for m in [-1, 1]:
            second = True
            nb = 0
            for _ in range(nb_accel):
                if nb % 2 == 0:
                    self.santa.accelerate('horizontal', m * a)
                else:
                    self.santa.accelerate('vertical', m * b)
                if second:
                    nb += 1
                second = not second

    def max_speed(self, weight):
        for k, v in self.game.acceleration_ranges.items():
            if k > weight:
                return v
        return 0

    def predict_carrots(self, gifts: list[Gift]):
        carrots = 0
        for gift in gifts:
            # TODO
            return 0
        return carrots
