import math

def part1():
  return count_slope(3)

def part2():
  return math.prod(count_slope(n) for n in [1,3,5,7,.5])

def count_slope(n):
  return sum(process_line(line.strip(),i,n) 
             for i, line in enumerate(open("input3.txt")))

def process_line(line,i,n):
  idx = (float(i)*n) % len(line)
  if not idx.is_integer():
    return 0
  return line[int(idx)] == '#'

