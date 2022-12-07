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


if __name__ == "__main__":
    print(enumerate_vectors(3))


def get_distance_x_or_y(x1, x2):
    return abs(x1 - x2)
