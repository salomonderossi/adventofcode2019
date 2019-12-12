#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
from collections import defaultdict

sys.setrecursionlimit(10000)
log = logging.getLogger(__name__)


class OrbitMap(object):
    def __init__(self, orbit_list):
        self.orbit_dict = defaultdict(list)
        for items in orbit_list:
            self.orbit_dict[items[0]].append(items[1])

    def __count_direct(self, orbit_name):
        ret = sum(self.__count_direct(o) for o in self.orbit_dict[orbit_name])
        ret += len(self.orbit_dict[orbit_name])
        return ret

    def __count_indirect(self):
        ret = 0
        for orbit_name in self.orbit_dict:
            if orbit_name == "COM":
                continue

            ret += self.__count_direct(orbit_name)

        return ret

    def count(self):
        #return self.__count_direct("COM")
        return self.__count_direct("COM") + self.__count_indirect()


def test():
    values = list()
    with open("input", "r") as f:
        values = f.readlines()
    orbits = [o.strip().split(")") for o in values]

    om = OrbitMap(orbits)
    #print([[o, om.orbit_dict[o]] for o in om.orbit_dict][:10])
    #print(om.orbit_dict["WLQ"])
    #print(len(om.orbit_dict["WLQ"]))

    #return
    print(om.count())


if __name__ == '__main__':
    import signal

    logging.basicConfig(level=logging.DEBUG)
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    #import cProfile
    #stats_file = "stats.prof"
    #cProfile.run("test()", stats_file)

    test()

    print("done")
