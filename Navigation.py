import Santa
from utils import get_distance_x_or_y


class Navigation:

    def __init__(self, santa: Santa):
        self.santa = santa

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
