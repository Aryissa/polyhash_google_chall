import math


def get_distance(x1, y1, x2, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return math.sqrt(dx ** 2 + dy ** 2)


def enumerate_vectors(max_speed: int):
    vectors = []
    for i in range(-max_speed, max_speed + 1):
        for j in range(-max_speed, max_speed + 1):
            if j != 0 and i != 0:
                vectors.append((i, j))
    return vectors


def enumerate_cases_in_range(x, y, r):
    coords = []
    for i in range(x - r, x + r + 1):
        for j in range(y - r, y + r + 1):
            if get_distance(x, y, i, j) <= r:
                coords.append((i, j))
    return coords

def gift_here(x, y, gifts):
    for gift in gifts:
        if gift.x == x and gift.y == y:
            return True
    return False


def gifts_in_range(x, y, r, gifts):
    return [g for g in gifts if get_distance(x, y, g.x, g.y) <= r]


if __name__ == "__main__":
    print(enumerate_vectors(3))


def get_distance_x_or_y(x1, x2):
    return abs(x1 - x2)
