#!/usr/bin/env python3
# coding: utf-8

import random
from math import ceil


class Chromosome:

    def __init__(self):
        self.genes = list()
        self.score = 0.0

    def __eq__(self, other):
        return self.genes == other.genes

    def __len__(self):
        return len(self.genes)

    def random_generate(self, size):
        self.genes = random.sample(range(0, size), size)

    def crossover_generate(self, first, second):
        self.genes = first.genes[0: ceil(len(first)/2)]
        for i in second.genes:
            if len(self) < len(first) and i not in self.genes:
                self.genes.append(i)

    def mutation_generate(self):
        second = first = random.randint(0, len(self) - 1)
        while second == first:
            second = random.randint(0, len(self) - 1)
        self.genes[first], self.genes[second] = self.genes[second], self.genes[first]

    def __str__(self):
        return "score: {}".format(self.score)
