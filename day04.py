import utils
import map
from map import Map
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day04_test.txt')
finput = os.path.join(dir, 'day04_input.txt')

@utils.timeit
def part1(fname):
    res = 0
    m = Map(fname)

    def check(m, p, s, d):
        l = list(s)
        for n in range(len(l)):
            xx = p.x + (n + 1) * d[0]
            yy = p.y + (n + 1) * d[1]
            c = m.get(xx, yy)
            cExp = l[n]
            if c != cExp:
                return False
        return True
    
    for p in m.findAll('X'):
        for d in map.ds:
            if check(m, p, 'MAS', d):
                res += 1
    return res

def do1():
    assert 18 == part1(ftest)
    assert 2521 == part1(finput)

@utils.timeit
def part2(fname):
    res = 0
    m = Map(fname)

    def get2(m, p, d1, d2):
        
        def get(m, p, d):
            res = m.get(p.x + d[0], p.y + d[1])
            return res if res else ''
        
        return get(m, p, d1) + get(m, p, d2)

    def ok(s):
        return s == 'MS' or s == 'SM'
    
    for p in m.findAll('A'):
        s1 = get2(m, p, map.dNW, map.dSE)
        s2 = get2(m, p, map.dNE, map.dSW)
        if ok(s1) and ok(s2):
            res += 1
    return res

def do2():
    assert 9 == part2(ftest)
    assert 1912 == part2(finput)
