import numpy as np
import itertools
import queue

data = [tuple(map(int, player_data.split("\n")[1:])) for player_data in open("input22.txt").read().split("\n\n")]
# data = np.array(data, dtype=int)


def score(p):
    return sum(c*(len(p)-i) for i, c in enumerate(p))


def game(h1, h2, recurse=False):
    done = False
    viewed_hands = set()
    while not done:

        hands = (tuple(h1), tuple(h2))
        if hands in viewed_hands:
            return score(h1), 1
        viewed_hands.add(hands)

        c1, *h1 = h1
        c2, *h2 = h2

        if recurse and len(h1) >= c1 and len(h2) >= c2:
            _, winner = game(h1[:c1], h2[:c2])
        else:
            winner = 1 if c1 > c2 else 2

        if winner == 1:
            h1 += [c1, c2]
        else:
            h2 += [c2, c1]
        done = len(h1) == 0 or len(h2) == 0
    winner = 1 if h1 else 2

    return score(h1 if winner==1 else h2), winner


def part1():
    h1, h2 = data
    return game(h1, h2)[0]


def part2():
    h1, h2 = data
    return game(h1, h2, True)[0]


if __name__ == "__main__":
    import main
    main.profile((part1, part2))
