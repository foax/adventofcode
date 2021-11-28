#!/usr/bin/env python3
import sys
import re
from pprint import pprint


class Bag:

    all_bags = {}
    all_bags_by_colour = {}

    @classmethod
    def bag_exists(cls, colour):
        return colour in cls.all_bags_by_colour

    @classmethod
    def get_bag_by_colour(cls, colour):
        return cls.all_bags_by_colour[colour]

    @classmethod
    def get_all_bags(cls):
        return cls.all_bags

    def __str__(self):
        return self.colour

    def __init__(self, colour):
        self.colour = colour
        self.contains = {}
        self.contained_in = {}
        self.all_bags[self] = True
        self.all_bags_by_colour[self.colour] = self

    def get_colour(self):
        return self.colour

    def set_contains(self, bag, count):
        self.contains[bag] = count

    def set_contained_in(self, bag):
        self.contained_in[bag] = True

    def get_contains(self):
        return self.contains

    def get_contained_in(self):
        return self.contained_in

    def get_outer_most_bags(self):
        already_found_set = set()

        for b in self.contained_in:
            already_found_set.add(b)
            already_found_set |= b.get_outer_most_bags()

        return already_found_set

    def count_containing_bags(self):
        total = 0

        for b, count in self.contains.items():
            # print(f'Self: {self}; Contains Bag: {b}; Count: {count}')
            c = b.count_containing_bags()
            # print(
            #   f'Bag: {b}; Containing bag count: {c}; number of bags: {count}')
            total += count * b.count_containing_bags() + count

        # print(f'Total: {total}')
        return total


for line in sys.stdin:
    match = re.match('(.+) bags contain (.+).', line.rstrip())
    colour, contents = match.group(1, 2)
    contents = contents.split(', ')
    # print(f'colour: {colour}; contents: {contents}')
    outer_bag = None
    if Bag.bag_exists(colour):
        outer_bag = Bag.get_bag_by_colour(colour)
    else:
        outer_bag = Bag(colour)

    for bag_spec in contents:
        if bag_spec == 'no other bags':
            break
        match = re.match('(\d+) (.+) bag', bag_spec)
        count, colour = match.group(1, 2)
        if not Bag.bag_exists(colour):
            new_bag = Bag(colour)
        inner_bag = Bag.get_bag_by_colour(colour)
        outer_bag.set_contains(inner_bag, int(count))
        inner_bag.set_contained_in(outer_bag)

outer_bag_count = 0
shiny_gold = Bag.get_bag_by_colour('shiny gold')
shiny_gold_outer_bags = shiny_gold.get_outer_most_bags()

print(f'Number of outer bags for shiny gold: {len(shiny_gold_outer_bags)}')

print(
    f'Number of inner bags for shiny gold: {shiny_gold.count_containing_bags()}')
