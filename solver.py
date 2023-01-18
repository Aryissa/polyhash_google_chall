#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module de résolution du projet Poly#.
"""

import utils
from Game import Game
from Santa import Santa
from Navigation import Navigation

def solve(challenge):
    """Résout un challenge donné.
    """

    score = -1
    best_santa = None
    for santa in [go_47_78(challenge)]:
        if santa.score > score:
            score = santa.score
            best_santa = santa

    print(f"\nScore : {best_santa.score}\nTemps : {best_santa.time}")
    return best_santa


def no_move(game, santa):
    for gift in utils.gifts_in_range(0, 0, game.range, game.gifts):
        santa.load_gift(gift)
        game.gifts.remove(gift)
        santa.deliver(gift)
    print(f'Score obtenu en ne bougeant pas : {santa.score}')


def line_strat(challenge):
    print('line strat')
    game = Game(challenge)
    santa = Santa(game)

    no_move(game, santa)

    navigation = Navigation(santa, game)

    navigation.run_line(1)
    return santa


def line_strat_full_speed(challenge):
    print('line full speed strat')
    print('line strat')
    game = Game(challenge)
    santa = Santa(game)

    no_move(game, santa)

    navigation = Navigation(santa, game)

    navigation.run_line(2)
    return santa


def go_point_strat(challenge):
    game = Game(challenge)
    game.gifts = sorted(game.gifts, key=lambda gift: gift.ratio, reverse=True)
    santa = Santa(game)
    navigation = Navigation(santa, game)
    no_move(game, santa)
    x = 0
    while santa.time < game.max_time:
        santa.load_gift(game.gifts[x])
        x += 1
        santa.load_carrot(13)
        navigation.go_point(santa.gifts[0].x, santa.gifts[0].y)
        if santa.x == santa.gifts[0].x and santa.y == santa.gifts[0].y:
            santa.deliver(santa.gifts[0])
            navigation.go_point(0, 0)
    return santa


def go_47_78(challenge):
    game = Game(challenge)
    game.gifts = sorted(game.gifts, key=lambda gift: gift.ratio, reverse=True)
    santa = Santa(game)
    santa.load_carrot(1999)
    navigation = Navigation(santa, game)
    no_move(game, santa)
    navigation.go_approximatif(60000, 60000)
    print(santa.x, santa.y)
    navigation.go_point(60000, 60000)
    print(santa.x, santa.y)
    return santa
