import collections
import numpy as np
import functools as ft

data = [line.strip() for line in open("input24.txt") if len(line) > 0]

directions = {
    "nw": (-1, 0),
    "ne": (-1, 1),
    "e": (0, 1),
    "se": (1, 0),
    "sw": (1, -1),
    "w": (0, -1),
}


def steps_to_position(steps):
    steps = list(steps[::-1])

    x, y = 0, 0
    while len(steps) > 0:
        direction = steps.pop()
        if direction not in directions:
            direction += steps.pop()
        dx, dy = directions[direction]
        x += dx
        y += dy
    return x, y


positions = [steps_to_position(line) for line in data]
positions = [pos for pos, count in collections.Counter(positions).items() if count % 2 == 1]


def part1():
    return len(positions)


def pass_day(mat):
    mat = trim_mat(mat)
    mat = np.pad(mat, 1)
    adj = sum(np.roll(mat, shift, (0, 1)) for shift in directions.values())
    # white = False
    # black = True

    res = mat.copy()
    res[mat & ((adj == 0) | (adj > 2))] = False
    res[~mat & (adj == 2)] = True

    return res


def trim_mat(mat):
    true_points = np.argwhere(mat)
    top_left = true_points.min(axis=0)
    bottom_right = true_points.max(axis=0)
    return mat[top_left[0]:bottom_right[0]+1,
               top_left[1]:bottom_right[1]+1]


def print_mat(mat):

    print("")
    for i, line in enumerate(mat):
        print(" "*i+" ".join(str(int(c)) if c else "." for c in line))
    print(np.sum(mat))


def part2():
    np_positions = np.array(positions)
    np_positions -= np.min(np_positions, axis=0)
    mat = np.full(np.max(np_positions, axis=0)+1, False)  # False=white
    for i, j in np_positions:
        mat[i, j] = True

    # print_mat(mat)
    for i in range(100):
        mat = pass_day(mat)
        # print_mat(mat)
    return np.sum(mat)

    # return np.array(positions)


if __name__ == "__main__":
    import main
    main.profile((part1, part2))
