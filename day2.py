def part1():
  return sum(map(process_line_1,open("input2.txt")))

def part2():
  return sum(map(process_line_2,open("input2.txt")))

def parse_line(line):
  line = line.rstrip("\n")
  rules,pwd = line.split(": ")
  limits,char = rules.split(" ")
  low,high = limits.split("-")
  low=int(low);high=int(high)
  return low,high,char,pwd

def process_line_1(line):
  low,high,char,pwd=parse_line(line)
  return low<=pwd.count(char)<=high

def process_line_2(line):
  low,high,char,pwd=parse_line(line)
  return (pwd[low-1]==char) ^ (pwd[high-1]==char)