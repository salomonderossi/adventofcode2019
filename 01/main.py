#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import math

log = logging.getLogger(__name__)


def recursive_calc_fuel(mass):
    res = (math.ceil(int(mass)//3) - 2)
    
    if res <= 0:
        return 0
    else:
        return res + recursive_calc_fuel(res)


def puzzle_first_half():
    with open("input", "r") as f:
        lines = f.readlines()
    
    result = sum([math.ceil((int(n)//3) - 2) for n in lines])
    print(result)

    
def puzzle_second_half():
    with open("input", "r") as f:
        lines = f.readlines()
    
    result = sum([recursive_calc_fuel(n) for n in lines])
    print(result)

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
