import re

rules={}
containing={}
for line in open("input7.txt"):
    key = re.search("([\w ]*) bags contain ",line).group(1)
    regex2=re.findall("([0-9]+) ([\w ]*) bag",line)
    rules[key] = list(map(lambda a: (int(a[0]), a[1]), regex2))
    containing[key] = set(map(lambda a: a[1], regex2))


searched_bags=set()
def part1():
    find_containers('shiny gold')
    return len(searched_bags)-1

def find_containers(treasure):
    if treasure in searched_bags: 
        return
    searched_bags.add(treasure)
    for bag, items in containing.items():
        if treasure in items:
            find_containers(bag)

found_containers_old=dict()
def find_containers_old(treasure):
    if treasure in found_containers_old: 
        return found_containers_old[treasure]
    s = set()
    for bag, items in containing.items():
        if treasure in items:
            s.add(bag)
            s=s.union(find_containers_old(bag))
    found_containers_old[treasure]=s
    return s

def part2():
    return count_items('shiny gold')-1

def count_items(bag):
    return 1+sum(count_items(sbag)*count for count,sbag in rules[bag])
