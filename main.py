from importlib import import_module
from time import time
from os import listdir

print(listdir())

def profile(day_idx, show_percentages):
    print(f'day{day_idx}')
    start = time()
    day=import_module(f'day{day_idx}') 
    after_import = time()
    res1=day.part1()
    after_res1 = time()
    res2=day.part2()
    end = time()
    print(f'part1: {res1}, part2: {res2}')
    duration = end - start
    print(f'It took {duration:.3f} seconds!')
    if show_percentages:
        percentage_i = (after_import - start)/duration
        percentage_1 = (after_res1 - after_import)/duration
        percentage_2 = (end - after_res1)/duration
        print(f'Split: {100*percentage_i:.1f}%i '+ 
                     f'{100*percentage_1:.1f}%1 '+ 
                     f'{100*percentage_2:.1f}%2 ')
    print('')
    return duration

total=sum(profile(i,True) for i in range(1,8))
print(f'Total is {total:3f}')