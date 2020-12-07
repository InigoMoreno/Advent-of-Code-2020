data=[int(line) for line in open("input1.txt")]
s = set(data)

def part1():
  for n in data:
    if 2020-n in s:
      return n*(2020-n)

def part2():
  for n1 in data:
    for n2 in data:
      if 2020-n1-n2 in s:
        return n1*n2*(2020-n1-n2)