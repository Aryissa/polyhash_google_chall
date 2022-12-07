import math


def get_distance(x1, y1, x2, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return math.sqrt(dx ** 2 + dy ** 2)


def get_distance_x(x1, x2):
    return abs(x1 - x2)


def get_distance_y(y1, y2):
    return abs(y1 - y2)
