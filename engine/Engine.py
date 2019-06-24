#!/usr/bin/env python3
# coding: utf-8
import copy
import json
import random

from engine.Chromosome import Chromosome
from engine.City import City


class Engine:

    def __init__(self, filename, sample):
        self.cities = list()
        self.chromosomes = list()
        self.new_chromosomes = list()
        self.best_itinary = None
        self.sample = sample
        self._parse_cities(filename)
        self._generate_sample(sample)

    def _parse_cities(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
        for d in data:
            self.cities.append(City(d["city"], d["lan"], d["lng"]))

    def _generate_sample(self, sample):
        self.chromosomes = [Chromosome() for x in range(sample)]
        [x.random_generate(len(self.cities)) for x in self.chromosomes]

    def _get_total_distance(self, chromosome):
        total = 0.0
        last = None
        for c in chromosome.genes:
            if last:
                total += self.cities[last].distance(self.cities[c])
            last = c
        return total

    def _evaluation(self):
        for c in self.chromosomes:
            c.score = self._get_total_distance(c)
            if self.best_itinary is None or c.score < self.best_itinary.score:
                self.best_itinary = c

    def _selection(self):
        self.chromosomes.sort(key=lambda x: x.score, reverse=False)
        self.chromosomes = self.chromosomes[0:self.sample]

    def _crossover(self):
        for x in self.chromosomes:
            first_child = Chromosome()
            second_child = Chromosome()
            first_child.crossover_generate(x, self.chromosomes[random.randint(0, len(self.chromosomes) - 1)])
            second_child.crossover_generate(self.chromosomes[random.randint(0, len(self.chromosomes) - 1)], x)
            self.new_chromosomes.append(first_child)
            self.new_chromosomes.append(second_child)

    def _mutation(self, percent=0.1):
        for x in self.chromosomes:
            if random.uniform(0.00, 100.00) <= percent:
                mutant = copy.deepcopy(x)
                mutant.mutation_generate()
                self.new_chromosomes.append(mutant)

    def _append_new_chromosomes(self):
        for x in self.new_chromosomes:
            if x not in self.chromosomes:
                self.chromosomes.append(x)

    def iteration(self):
        #print("selection")
        self._selection()
        self.new_chromosomes = list()
        #print("crossover")
        self._crossover()
        #print("mutation")
        self._mutation()
        #print("append new chromosomes")
        self._append_new_chromosomes()
        # print("evaluation")
        self._evaluation()

    def get_best_iteraton_city(self):
        return [self.cities[x].name for x in self.best_itinary.genes]
