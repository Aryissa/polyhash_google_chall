#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module principal pour la mise en oeuvre du projet Poly#.
"""
from Navigation import Navigation
from Santa import Santa
# Vous pouvez structurer votre code en modules pour améliorer la
# compréhension et faciliter le travail collaboratif
from parser_challenge import parse_challenge
from solver import solve
# from scorer import score_solution
from Game import Game

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
    # solution = solve(challenge)
    # print(f"Score: {score_solution(solution)}")
    santa = Santa(game)
    navigation = Navigation(santa)

    game.gifts = sorted(game.gifts, key=lambda gift: gift.ratio)

    x = 0
    while santa.time < game.max_time:
        santa.load_gift(game.gifts[x])
        x += 1
        santa.load_carrot(10)
        navigation.go_point(santa.gifts[0].x, santa.gifts[0].y)
        santa.deliver(santa.gifts[0])
        navigation.go_point(0, 0)

    print(santa.print())
    print(santa.score)
