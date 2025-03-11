import utils
import map
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day04_test.txt')
finput = os.path.join(dir, 'day04_input.txt')

def checkP1(m, p, s, d):
    l = list(s)
    for n in range(len(l)):
        xx = p.x + (n + 1) * d[0]
        yy = p.y + (n + 1) * d[1]
        c = m.get(xx, yy)
        cExp = l[n]
        if c != cExp:
            return False
    return True

@utils.timeit
def part1(fname):
    res = 0
    m = map.Map(fname)
    for p in m.findAll('X'):
        for d in map.ds:
            if checkP1(m, p, 'MAS', d):
                res += 1
    return res

def do1():
    print(18 == part1(ftest))
    print(part1(finput))
    #2521

def get1(m, p, d):
    res = m.get(p.x + d[0], p.y + d[1])
    return res if res else ''

def get2(m, p, d1, d2):
    return get1(m, p, d1) + get1(m, p, d2)

def ok(s):
    return s == 'MS' or s == 'SM'

@utils.timeit
def part2(fname):
    res = 0
    m = map.Map(fname)
    for p in m.findAll('A'):
        s1 = get2(m, p, map.dNW, map.dSE)
        s2 = get2(m, p, map.dNE, map.dSW)
        if ok(s1) and ok(s2):
            res += 1
    return res

def do2():
    print(9 == part2(ftest))
    print(part2(finput))
    #1912
