import numpy as np
import itertools
import queue
import collections

data = [line.strip()[:-len(")")].split(" (") for line in open("input21.txt")]
data = [(a.split(" "), b[len("contains "):].split(", ")) for [a, b] in data]

ingredient_count = collections.Counter([ing for a, _ in data for ing in a])
ingredients = list(ingredient_count.keys())
alergens = list(set([ale for _, b in data for ale in b]))
safe_ingredients = None

def part1():
    global safe_ingredients
    table = np.array([
        [
            all(ing in si for si, sa in data if ale in sa)
            for ale in alergens
        ]
        for ing in ingredients
    ])

    safe_ingredients = [ing for ing, row in zip(ingredients, table) if np.all(~row)]
    return sum(ingredient_count[ing] for ing in safe_ingredients)


def part2():
    global safe_ingredients
    if safe_ingredients is None:
        part1()

    possible_ingredients = list(set(ingredients)-set(safe_ingredients))

    table = np.array([
        [
            all(ing in si for si, sa in data if ale in sa)
            for ale in alergens
        ]
        for ing in possible_ingredients
    ])

    known_pairs = []

    while np.any(np.sum(table, axis=1) == 1):
        for i in np.ravel(np.argwhere(np.sum(table, axis=1) == 1)):
            j = np.argwhere(table[i,:])[0][0]
            known_pairs.append((alergens[j], possible_ingredients[i]))
            table = np.delete(table, i, 0)
            table = np.delete(table, j, 1)
            del possible_ingredients[i]
            del alergens[j]

    return ",".join(b for _,b in sorted(known_pairs))


if __name__ == "__main__":
    import main
    main.profile((part1, part2))
