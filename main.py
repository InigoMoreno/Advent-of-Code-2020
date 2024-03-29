from importlib import import_module
from time import time
from os import listdir
import re


def profile(day, show_percentages=False):
    start = time()
    match day:
        case tuple((part1, part2)):
            after_import = time()
            pass
        case int(day_idx):
            print(f'day{day_idx}')
            day_module = import_module(f'day{day_idx}')
            after_import = time()
            part1, part2 = day_module.part1, day_module.part2
    res1 = part1()
    after_res1 = time()
    print(f'part1: {res1}', end="", flush=True)
    res2 = part2()
    end = time()
    print(f', part2: {res2}')
    duration = end - start
    print(f'It took {duration:.3f} seconds!')
    if show_percentages:
        percentage_i = (after_import - start)/duration
        percentage_1 = (after_res1 - after_import)/duration
        percentage_2 = (end - after_res1)/duration
        print(f'Split: {100*percentage_i:.1f}%i ' +
              f'{100*percentage_1:.1f}%1 ' +
              f'{100*percentage_2:.1f}%2 ')
    print('')
    return duration


matches = [re.match('day([0-9]+).py', dir) for dir in listdir()]
last = max(int(match.group(1)) for match in matches if match is not None)


def profile_all(show_percentages):
    total = sum(profile(i, show_percentages) for i in range(1, last+1))
    print(f'Total is {total:3f}')


def run_last():
    day = import_module(f'day{last}')
    print(f'part1: {day.part1()}, part2: {day.part2()}')


if __name__ == "__main__":
    profile_all(False)
    # run_last()
