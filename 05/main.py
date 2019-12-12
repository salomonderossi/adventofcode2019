#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from functools import reduce

log = logging.getLogger(__name__)


class GravityAssist(object):
    def __init__(self, values):
        self.values = values.copy()
        self.opcode_pointer = 0
        self.output_list = list()

        self.__states = {1: self.sum,
                         2: self.mul,
                         3: self.store,
                         4: self.output,
                         99: self.end}

    def __get_opcode_values(self, parameter_mode):
        result = list()
        for i, mode in enumerate(parameter_mode):
            value = self.values[self.opcode_pointer+i]
            if mode == 1:
                value = self.values[value]
            result.append(value)

        return result
        #value_1 = self.values[self.opcode_pointer+1]
        #if parameter_mode[0] == 1:
        #    position_1 = self.values[self.opcode_pointer+1]
        #    value_1 = self.values[position_1]
        # 
        #value_3 = self.values[self.opcode_pointer+2]
        #if parameter_mode[1] == 1:
        #    position_2 = self.values[self.opcode_pointer+2]
        #    value_2 = self.values[position_2]
        # 
        #value_3 = self.values[self.opcode_pointer+3]
        #if parameter_mode[2] == 1:
        #    position_3 = self.values[self.opcode_pointer+2]
        #    value_3 = self.values[position_3]
        # 
        #return value_1, value_2, value_3

    def get_current_opcode(self, parameter_mode):
        optcode = int(str(self.values[self.opcode_pointer])[-2:])
        parameter_mode = list(str(self.values[self.opcode_pointer])[:-2])
        return optcode, parameter_mode

    def run(self):
        try:
            opcode = 1
            while(opcode != 99):
                opcode, parameter_mode = self.get_current_opcode()
                self.__states[opcode](parameter_mode)
        except KeyError:
            log.error("Could not handle opcode: %s", opcode)
            log.error("Program cannot continue")
            return False
        return True

    def sum(self, parameter_mode):
        try:
            values = self.__get_opcode_values()
            self.values[values[-1]] = reduce(lambda x, y: x+y, values[:-1])

            self.opcode_pointer += len(values+1)
            
            #value_1, value_2, value_3 = self.__get_opcode_values()
            #self.values[value_3] = value_1 + value_2
            # 
            #self.opcode_pointer += self.__opcode_increment
            return True
        except IndexError:
            log.error("Could not assign value: %s", self.opcode_pointer)
            log.error("Program cannot continue")
            return False

    def mul(self, parameter_mode):
        try:
            values = self.__get_opcode_values()
            self.values[values[-1]] = reduce(lambda x, y: x*y, values[:-1])

            self.opcode_pointer += len(values+1)
            
            #value_1, value_2, value_3 = self.__get_opcode_values()
            #self.values[value_3] = value_1 * value_2
            # 
            #self.opcode_pointer += self.__opcode_increment
            return True
        except IndexError:
            log.error("Could not assign value: %s", self.opcode_pointer)
            log.error("Program cannot continue")
            return False

    def store(self, parameter_mode):
        try:
            values = self.__get_opcode_values()
            self.values[values[1]] = values[0]

            self.opcode_pointer += len(values+1)
            return True
        except IndexError:
            log.error("Could not assign value: %s", self.opcode_pointer)
            log.error("Program cannot continue")
            return False

    def output(self, parameter_mode):
        try:
            values = self.__get_opcode_values()
            self.output_list.append(valü[0])

            self.opcode_pointer += len(values+1)
            return True
        except IndexError:
            log.error("Could not assign value: %s", self.opcode_pointer)
            log.error("Program cannot continue")
            return False

    def end(self, parameter_mode):
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
