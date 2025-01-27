#!/usr/bin/python3

"""Script that read stdin line by line and computes metrics"""

import sys


def printsts(dic, size):
    """ WWPrints information """
    print("File size: {:d}".format(size))
    for z in sorted(dic.keys()):
        if dic[z] != 0:
            print("{}: {:d}".format(z, dic[z]))


sts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}

count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            printsts(sts, size)

        stlist = line.split()
        count += 1

        try:
            size += int(stlist[-1])
        except:
            pass

        try:
            if stlist[-2] in sts:
                sts[stlist[-2]] += 1
        except:
            pass
    printsts(sts, size)


except KeyboardInterrupt:
    printsts(sts, size)
    raise