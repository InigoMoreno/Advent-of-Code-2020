import numpy as np
import itertools
import queue

data = list(map(int, open("input23.txt").read().strip()))
# data = np.array(data, dtype=int)


def move(circle, moves=1):
    N = len(circle)

    nex = [i + 1 for i in range(N + 1)]
    for i in range(N):
        nex[circle[i-1]] = circle[i]

    head = circle[0]

    for _ in range(moves):
        # head, p1, p2, p3, *rest = circle

        rem1 = nex[head]
        rem2 = nex[rem1]
        rem3 = nex[rem2]
        m = rem1, rem2, rem3 # 3 after current
        nex[head]=nex[rem3] # remove them from linked list by pointing head to the one after


        looking_for = head-1 or N
        while looking_for in m:
            looking_for = looking_for-1 or N

        # put rem1,rem2,rem3 after between looking_for and nex[looking_for]
        nex[rem3] = nex[looking_for]
        nex[looking_for] = rem1

        # i = circle.index(looking_for)
        # circle = rest[:i+1] + list(m) + rest[i+1:] + [head]

        # select new current cup
        head = nex[head]

    cup = nex[1]
    while cup != 1:
        yield cup
        cup = nex[cup]



def part1():
    circle = data
    circle = move(circle, 100)
    res = "".join(map(str, circle))
    return res


def part2():
    N = 1000000
    circle = data + list(range(10, N+1))
    circle = move(circle, 10*N)
    return next(circle)*next(circle)


if __name__ == "__main__":
    import main
    main.profile((part1, part2))
