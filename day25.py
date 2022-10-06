import numpy as np
import itertools
import queue
import collections

n = 20201227

a, b = map(int, open("input25.txt"))


def encrypt(i, k):
    v = 1
    for _ in range(k):
        v = v*i % n
    return v


def decrypt(i, v):
    mv = 1
    for k in itertools.count(start=1):
        mv = mv*i % n
        if v==mv:
            return k


def part1():
    kb = decrypt(7, b)
    return encrypt(a,kb)


def part2():
    return None


if __name__ == "__main__":
    import main
    main.profile((part1, part2))
