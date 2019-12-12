#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging


log = logging.getLogger(__name__)


def check_password(p):
    # check if lenght is 6
    if len(p) != 6:
        return False

    # check if there are at least two adjacent digits
    adjacent = 0
    for i in range(len(p)):
        try:
            if p[i] == p[i+1]:
                adjacent += 1
        except IndexError:
            break
        else:
            continue
    if adjacent == 0:
        return False

    # check if the digits increase
    for i in range(len(p)):
        try:
            if p[i] > p[i+1]:
                return False
        except IndexError:
            break
    return True


def test():
    valid_passwords = 0
    for i in range(168630, 718098+1):
        p = [int(x) for x in str(i)]
        if check_password(p) is True:
            valid_passwords += 1

    print(valid_passwords)
        

if __name__ == '__main__':
    import signal

    logging.basicConfig(level=logging.DEBUG)
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    #import cProfile
    #stats_file = "stats.prof"
    #cProfile.run("test()", stats_file)

    test()

    print("done")
