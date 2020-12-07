from functools import reduce

def main(fun):
    return sum(
        len(reduce(fun,[set(line) for line in block.split('\n')])) 
        for block in open("input6.txt").read().split("\n\n")
    )

def part1():
    return main(set.union)

def part2():
    return main(set.intersection)