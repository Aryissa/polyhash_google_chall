#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module principal pour la mise en oeuvre du projet Poly#.
"""
import matplotlib.pyplot as plt

import utils
from Navigation import Navigation
from Santa import Santa
# Vous pouvez structurer votre code en modules pour améliorer la
# compréhension et faciliter le travail collaboratif
from parser_challenge import parse_challenge
from solver import solve
# from scorer import score_solution
from Game import Game
from Map import Map
from Zone import Zone
from pprint import pprint

if __name__ == "__main__":
    # On fournit ici un exemple permettant de passer un simple
    # argument (le fichier du challenge) en paramètre. N'hésitez pas à
    # compléter avec d'autres paramètres/options.
    import argparse
    parser = argparse.ArgumentParser(description='Solve Poly# challenge.')
    parser.add_argument('challenge', type=str,
                        help='challenge definition filename',
                        metavar="challenge.txt")
    args = parser.parse_args()

    challenge = parse_challenge(args.challenge)
    game = Game(challenge)
    print("=============")
    print("Polyhash 2022")
    print("=============")
    print(f"Challenge {args.challenge}\n")
    print(game)
    # solution = solve(challenge)
    # print(f"Score: {score_solution(solution)}")
    santa = Santa(game)

    map = Map(game.gifts)
    zone = Zone(game.gifts)
    moyenne= zone.moyenne_points(map,santa)
    print("MOYENNE",moyenne)
    cluster = zone.clusterisation(moyenne)
    print("TAILLE DU CLUSTER", len(cluster))
    print("SCORE CLUSTER", zone.calcul_score_total_cluster())


    #solution = solve(challenge)
    #print(f"Score: {score_solution(solution)}")
    navigation = Navigation(santa, game)
    game.gifts = sorted(game.gifts, key=lambda gift: gift.ratio)

    for gift in utils.gifts_in_range(0, 0, game.range, game.gifts):
        santa.load_gift(gift)
        game.gifts.remove(gift)
        santa.deliver(gift)
    print(f'Score obtenu en ne bougeant pas : {santa.score}')

    if False:
        x = 0
        while santa.time < game.max_time:
            santa.load_gift(game.gifts[x])
            x += 1
            santa.load_carrot(10)
            navigation.go_point(santa.gifts[0].x, santa.gifts[0].y)
            santa.deliver(santa.gifts[0])
            navigation.go_point(0, 0)
    else:
        while False:
            action = navigation.lines_r_actions(0, 0)
            if santa.time + action['time'] > game.max_time:
                break
            navigation.lines_r_navigate_x(action)
    santa.print()
    print(f"\nScore : {santa.score}\nTemps : {santa.time}/{game.max_time}")

    santa.affichage()
    plt.show()
