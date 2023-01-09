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


    """map = Map(game.gifts)
    zone = Zone(game.gifts)
    moyenne = zone.moyenne_points(map,140000,game.gifts)
    print(moyenne)
    cluster = zone.clusterisation(moyenne)
    print("TAILLE DU CLUSTER", len(cluster))"""

    santa = solve(challenge)

    santa.print()
    print(f"\nScore : {santa.score}\nTemps : {santa.time}/{game.max_time}")

    santa.affichage()
    plt.show()
