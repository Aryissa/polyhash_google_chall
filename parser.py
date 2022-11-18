#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module de parsing des fichiers d'entrée pour la mise en oeuvre du projet Poly#.
"""
from pprint import pprint


def parse_challenge(filename: str) -> object:
    challenge = dict()
    with open(filename, 'r') as infile:  # ouverture du fichier (mode r: read)
        data = infile.read()  # lecture du contenu du fichier
    """Lit un fichier de challenge et extrait les informations nécessaires.
    """
    lines = data.split('\n')

    first_line = lines[0].split(' ')
    challenge["time"] = first_line[0]
    challenge["delivery_distance"] = first_line[1]
    challenge["acceleration_ranges"] = first_line[2]
    challenge["nb_gifts"] = first_line[3]
    lines.pop(0)

    challenge["gifts_list"] = []
    challenge["accelerations"] = []
    last_weight = 0
    for i in lines:
        line_content = i.split(' ')
        if len(i) == 0:
            continue
        if len(line_content) > 2:
            challenge["gifts_list"].append({"name": line_content[0],
                                            "score": line_content[1],
                                            "weight": line_content[2],
                                            "x": line_content[3],
                                            "y": line_content[4]})
        else:
            #print(line_content)
            challenge["accelerations"].append({"weight_interval_from": last_weight,
                                               "weight_interval_to": line_content[0],
                                               "max_acceleration": line_content[1]})
            last_weight = line_content[0]

    return challenge


if __name__ == '__main__':
    pprint(parse_challenge("input/e_excellent_weather.in.txt"))
