import re

starting = {
    "byr": False,
    "iyr": False,
    "eyr": False,
    "hgt": False,
    "hcl": False,
    "ecl": False,
    "pid": False
}

def part1():
    return main(False)
def part2():
    return main(True)

lines= [block.replace('\n',' ')
       for block in open("input4.txt").read().split("\n\n")]

def main(check_items):
    return sum(check_line(line, check_items)
               for line in lines)

def check_line(line,check_items):
    d=starting.copy()
    for keyitem in line.split(" "):
        key,item = keyitem.split(":")
        if key in d.keys():
            d[key] = d[key] or not check_items or checkitem(key,item)
    return all(d.values())

    
def checkbyr(item):
    try: return 1920<=int(item)<=2002
    except ValueError: return False

def checkiyr(item):
    try: return 2010<=int(item)<=2020
    except ValueError: return False

def checkeyr(item):
    try: return 2020<=int(item)<=2030
    except ValueError: return False

def checkhgt(item):
    try:
        if item.endswith("cm"):
            return 150<=int(item[:-2])<=193
        elif  item.endswith("in"):
            return 59<=int(item[:-2])<=76
        else: return False
    except ValueError: return False

def checkhcl(item):
    return len(item)==7 and re.search("#[0-9a-f]{6}",item)


def checkecl(item):
    return item in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def checkpid(item):
    return len(item)==9 and re.search("[0-9]{9}",item)

switcher = {
    "byr": checkbyr,
    "iyr": checkiyr,
    "eyr": checkeyr,
    "hgt": checkhgt,
    "hcl": checkhcl,
    "ecl": checkecl,
    "pid": checkpid
}

def checkitem(key,item):
    checker = switcher[key]
    return bool(checker(item))
