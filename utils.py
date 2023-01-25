import math


def get_distance(x1, y1, x2, y2):
    """Donne la distance exacte entre 2 points"""
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return math.sqrt(dx ** 2 + dy ** 2)


def enumerate_vectors(max_speed: int):
    """Enumere tous les vecteurs possibles avec une vitesse maximum donnée (max 15)"""
    max_speed %= 15
    vectors = []
    for i in range(-max_speed, max_speed + 1):
        for j in range(-max_speed, max_speed + 1):
            if j != 0 or i != 0:
                vectors.append((i, j))
    return vectors


def gift_here(x: int, y: int, gifts: list):
    """Return True s'il y a un cadeau à ces coordonnées"""
    for gift in gifts:
        if gift.x == x and gift.y == y:
            return True
    return False


def gifts_in_range(x: int, y: int, delivery_range: int, gifts: list):
    """Renvoie une liste des cadeaux atteignables avec la distance de livraison donnée"""
    return [g for g in gifts if get_distance(x, y, g.x, g.y) <= delivery_range]


def get_distance_x_or_y(x1, x2):
    """Donne la distance entre deux entiers"""
    return abs(x1 - x2)


def diviseur(nb):
    res = 1
    while nb // 10 >= 10:
        nb //= 10
        res *= 10
    return res

def gift_plus_proche(cluster,santa_x,santa_y):
    gift_proche=cluster[0]
    for gift in cluster:
        if get_distance(gift_proche.x,gift_proche.y,santa_x,santa_y)>get_distance(gift.x,gift.y,santa_x,santa_y):
            gift_proche=gift
    return gift_proche


if __name__ == "__main__":
    print(enumerate_vectors(3))
