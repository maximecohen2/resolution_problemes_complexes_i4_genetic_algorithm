#!/usr/bin/env python3
# coding: utf-8

import argparse

from engine import Engine


def parse_args():
    parser = argparse.ArgumentParser(description="Algorithme génétique de reccherche de chemin",
                                     usage="%(prog)s [OPTIONAL] <FichierJson>")
    parser.add_argument("datafile", metavar="FichierJson", help="Chemin du fichier json")
    parser.add_argument("--sample", metavar="sample", default=400,
                        help="Nombre d'échantillon sélectionné à chaque itération")
    parser.add_argument("--iteration", metavar="iteration", default=200,
                        help="Nombre d'itération")
    args = parser.parse_args()
    return args


def check_args(args):
    pass


def main():
    args = parse_args()
    check_args(args)
    engine = Engine(args.datafile, args.sample)
    best_itinary = None
    for i in range(args.iteration):
        engine.iteration()
        best_itinary = engine.best_itinary
        print("Le meilleur itinéraire est de {:.2f} km".format(best_itinary.score))
    print("Le meilleur itinéraire trouvé avec {:.2f} km est {}".format(best_itinary.score,
                                                                       " - ".join(engine.get_best_iteraton_city())))


if __name__ == '__main__':
    main()
