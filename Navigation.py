import Game
from Gift import Gift
import Santa
from utils import get_distance_x_or_y, enumerate_vectors, enumerate_cases_in_range, gift_here, gifts_in_range, gift_plus_proche,gifts_in_range


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

    def line_r(self, x, y):
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
                x_res = x + (b / a) * gift.x + b
                y_res = x + (b / a) * gift.x - b
                if y + gift.y + self.game.range >= x_res >= y + gift.y - self.game.range:
                    v.append(gift)
                if y + gift.y + self.game.range >= y_res >= y + gift.y - self.game.range:
                    h.append(gift)
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
        self.santa.load_carrot(7)
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

    def max_speed(self, weight):
        for k, v in self.game.acceleration_ranges.items():
            if k > weight:
                return v
        return 0

    def predict_carrots(self, moyenne_dist_cadeaux):
        nb_carrots=0
        if self.game.range> moyenne_dist_cadeaux:
            nb_carrots=(len(self.santa.gifts)*(moyenne_dist_cadeaux/self.santa.max_speed()))/2
        else:
            nb_carrots=(len(self.santa.gifts)*(moyenne_dist_cadeaux/self.santa.max_speed()))
        return int(nb_carrots)
    

    def chemin_kruskal(self,cluster,santa):
        list_cadeau_visite=[]
        cluster_copy=[g for g in cluster]
        gift_proche=gift_plus_proche(cluster_copy,santa.x,santa.y)
        list_cadeau_visite.append(gift_proche)
        cluster_copy.remove(gift_proche)
        while len(list_cadeau_visite)<len(cluster):
            gift_proche=gift_plus_proche(cluster_copy,gift_proche.x,gift_proche.y)
            list_cadeau_visite.append(gift_proche)
            cluster_copy.remove(gift_proche)
        return list_cadeau_visite
    

    

    def deplacement_cluster(self,cluster,santa,max_weight,moyenne):
        #init chemin
        chemin=self.chemin_kruskal(cluster,santa)
        taille_chemin=len(chemin)
        #Si on est au dépot
        while santa.time<self.game.max_time or taille_chemin!=0:
            if santa.x==0 and santa.y==0:
                for i in range (0,len(chemin)):
                    if(santa.weight+chemin[i].weight<max_weight):
                        santa.load_gift(chemin[i])
                    else:
                        if(len(santa.gifts)!=0):
                            santa.load_carrot(max_weight-santa.weight-1)
                            prediction_carrots=self.predict_carrots(moyenne)-santa.nb_carrots-1
                            while (santa.nb_carrots<prediction_carrots):
                                santa.gifts.pop()
                                santa.load_carrot(abs(santa.nb_carrots-max_weight-santa.weight))
                        break
        # Poser des cadeaux
            santa.gifts=list(set(santa.gifts))
            carrot_rentre_maison=0
            print("carrote rentrer maison: ",carrot_rentre_maison)
            while (len(santa.gifts)!=0 and santa.nb_carrots>carrot_rentre_maison and santa.time<self.game.max_time):
                x=santa.gifts[0].x
                y=santa.gifts[0].y
                self.go_point(x,y)
                copy_santa_gift=[g for g in santa.gifts]
                for gift in copy_santa_gift:
                    if len(gifts_in_range(x, y, self.game.range, [gift]))!=0:
                        santa.deliver(gift)
                        chemin.remove(gift)
                        taille_chemin=taille_chemin-1

            self.go_point(0,0)
        self.go_point(0,0)


                

