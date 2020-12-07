
def part1():
    return max(ids)

def part2():
    s=set(ids)
    first=next(id for id in range(128*8) if id in s)
    return next(id for id in range(first,128*8) if id not in s)

def getid(line):
    line = line.strip()
    row = getpos('F',line[:7],0,127)
    col = getpos('L',line[-3:],0,8)
    return row*8 + col

def getpos(f,line,mn,mx):
    if len(line)==0: return int(mn)
    r=mx-mn+1
    if line[0]==f: return getpos(f,line[1:],mn,mx-r/2)
    else: return getpos(f,line[1:],mn+r/2,mx)

ids=[getid(line) for line in open("input5.txt")]
