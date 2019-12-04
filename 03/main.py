#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

log = logging.getLogger(__name__)


class WireRunner(object):
    def __init__(self):
        self.__command_list = {"L": self.__left,
                               "R": self.__right,
                               "U": self.__up,
                               "D": self.__down}

    def run_wire(self, wire, coordinates_visited):
        #log.debug("******************** Run started")
        for command in wire:
            direction, value = command[0], int(command[1:])
            #log.debug("Processing command: %s", command)
            coordinates_visited = self.__command_list[direction](value, coordinates_visited)
            #log.debug("Last coordinate: %s", coordinates_visited[-1])

        return set(coordinates_visited)

    def __left(self, value, coordinates_visited):
        if len(coordinates_visited) <= 0:
            start_x = 0
            start_y = 0
        else:
            start_x, start_y = coordinates_visited[-1]
            
        for i in range(value):
            #coordinates_visited.append(frozenset([start_x-1, start_y]))
            coordinates_visited.append(tuple([start_x-1, start_y]))
            start_x -= 1

        return coordinates_visited

    def __right(self, value, coordinates_visited):
        if len(coordinates_visited) <= 0:
            start_x = 0
            start_y = 0
        else:
            start_x, start_y = coordinates_visited[-1]
            
        for i in range(value):
            #coordinates_visited.append(frozenset([start_x+1, start_y]))
            coordinates_visited.append(tuple([start_x+1, start_y]))
            start_x += 1

        return coordinates_visited

    def __up(self, value, coordinates_visited):
        if len(coordinates_visited) <= 0:
            start_x = 0
            start_y = 0
        else:
            start_x, start_y = coordinates_visited[-1]
            
        for i in range(value):
            #coordinates_visited.append(frozenset([start_x, start_y+1]))
            coordinates_visited.append(tuple([start_x, start_y+1]))
            start_y += 1

        return coordinates_visited

    def __down(self, value, coordinates_visited):
        if len(coordinates_visited) <= 0:
            start_x = 0
            start_y = 0
        else:
            start_x, start_y = coordinates_visited[-1]
            
        for i in range(value):
            #coordinates_visited.append(frozenset([start_x, start_y-1]))
            coordinates_visited.append(tuple([start_x, start_y-1]))
            start_y -= 1

        return coordinates_visited


def puzzle_first_half():
    values = list()
    with open("input", "r") as f:
        values = f.readlines()
    wire_1, wire_2 = values[0].strip().split(","), values[1].strip().split(",")

    wr = WireRunner()
    wire_1_visited = list()
    wire_2_visited = list()

    wire_1_visited = wr.run_wire(wire_1, wire_1_visited)
    wire_2_visited = wr.run_wire(wire_2, wire_2_visited)

    # insersect the two wires
    intersections = [val for val in wire_1_visited if val in wire_2_visited]

    # calculate the hammming distance and get the smalles value
    min_distance = min([abs(i[0]) + abs(i[1]) for i in intersections])
    print(min_distance)


def puzzle_second_half():
    values = list()
    with open("input", "r") as f:
        values = f.readlines()
    wire_1, wire_2 = values[0].split(","), values[1].split(",")

    wr = WireRunner()


if __name__ == '__main__':
    import signal

    logging.basicConfig(level=logging.DEBUG)
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    #import cProfile
    #stats_file = "stats.prof"
    #cProfile.run("test()", stats_file)

    puzzle_first_half()
    puzzle_second_half()

    print("done")
