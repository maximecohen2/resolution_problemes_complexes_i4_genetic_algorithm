#!/usr/bin/env python3
# coding: utf-8

from math import radians, sin, cos, acos


class City:

    def __init__(self, name, lan, lng):
        self.name = name
        self.coord = (radians(lan), radians(lng))

    def distance(self, other):
        slat, slon = self.coord
        elat, elon = other.coord
        return 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))

    def __str__(self):
        return "City: {}".format(self.name)
