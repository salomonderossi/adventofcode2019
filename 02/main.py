#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

log = logging.getLogger(__name__)


class GravityAssist(object):
    def __init__(self, values):
        self.values = values.copy()
        self.opcode_pointer = 0

        self.__opcode_increment = 4
        self.__states = {1:  self.sum,
                         2:  self.mul,
                         99: self.end}

    def __get_opcode_values(self):
        position_1 = self.values[self.opcode_pointer+1]
        position_2 = self.values[self.opcode_pointer+2]

        value_1 = self.values[position_1]
        value_2 = self.values[position_2]
        value_3 = self.values[self.opcode_pointer+3]

        return value_1, value_2, value_3

    def get_current_opcode(self):
        return self.values[self.opcode_pointer]

    def run(self):
        try:
            opcode = 1
            while(opcode != 99):
                opcode = self.get_current_opcode()
                self.__states[opcode]()
        except KeyError:
            log.error("Could not handle opcode: %s", opcode)
            log.error("Program cannot continue")
            #print(self.values)
            return False
        return True

    def sum(self):
        try:
            value_1, value_2, value_3 = self.__get_opcode_values()
            self.values[value_3] = value_1 + value_2

            self.opcode_pointer += self.__opcode_increment
            return True
        except IndexError:
            log.error("Could not assign value: %s", self.opcode_pointer)
            log.error("Program cannot continue")
            return False

    def mul(self):
        try:
            value_1, value_2, value_3 = self.__get_opcode_values()
            self.values[value_3] = value_1 * value_2

            self.opcode_pointer += self.__opcode_increment
            return True
        except IndexError:
            log.error("Could not assign value: %s", self.opcode_pointer)
            log.error("Program cannot continue")
            return False

    def end(self):
        return True

    
def puzzle_first_half():
    values = list()
    with open("input", "r") as f:
        raw_content = f.read().strip()
        values = raw_content.split(",")
    values = [int(i) for i in values]

    ga = GravityAssist(values)
    ga.run()
    print(ga.values)

    
def puzzle_second_half():
    values = list()
    with open("input", "r") as f:
        raw_content = f.read().strip()
        values = raw_content.split(",")
    values = [int(i) for i in values]

    for i in range(0, 100):
        for j in range(0, 100):
            values[1] = j
            values[2] = i

            ga = GravityAssist(values)
            ga.run()

            if ga.values[0] == 19690720:
                print("%i %i %i" % (ga.values[0], ga.values[1], ga.values[2]))
                return


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
