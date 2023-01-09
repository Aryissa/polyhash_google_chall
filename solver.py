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

    score = 0
    best_santa = None
    for santa in [line_strat(challenge),
                  line_strat_full_speed(challenge)]:
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
