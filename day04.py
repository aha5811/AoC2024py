import utils
import maps
from maps import Map, Pos
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day04_test.txt')
finput = os.path.join(dir, 'day04_input.txt')

@utils.timeit
def part1(fname):
    res = 0
    m = Map(fname)

    def check(p: Pos, s: str, d: tuple[int]) -> bool:
        sl = list(s) # string to character list
        for n in range(len(sl)):
            xx = p.x + (n + 1) * d[0]
            yy = p.y + (n + 1) * d[1]
            if m.get(xx, yy) != sl[n]:
                return False
        return True
    
    for p in m.find_all('X'):
        for d in maps.ds:
            if check(p, 'MAS', d):
                res += 1
    return res

def do1():
    assert 18 == part1(ftest)
    assert 2521 == part1(finput)

@utils.timeit
def part2(fname):
    res = 0
    m = Map(fname)

    def get2(p: Pos, d1, d2) -> str:
        
        def get(p: Pos, d) -> str:
            s = m.get(p.x + d[0], p.y + d[1])
            return s if s else ''
        
        return get(p, d1) + get(p, d2)

    def ok(s: str) -> bool:
        return s == 'MS' or s == 'SM'
    
    for p in m.find_all('A'):
        s1 = get2(p, maps.dNW, maps.dSE)
        s2 = get2(p, maps.dNE, maps.dSW)
        if ok(s1) and ok(s2):
            res += 1
    return res

def do2():
    assert 9 == part2(ftest)
    assert 1912 == part2(finput)
