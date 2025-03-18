import utils
from utils import xor
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day02_test.txt')
finput = os.path.join(dir, 'day02_input.txt')

def check(ns):
    v = ns[0]
    inc = ns[1] > v
    for n in range(1, len(ns)):
        vv = ns[n]
        if xor(vv > v, inc):
            return False
        if vv == v or abs(vv - v) > 3: # difference not in [1, 2, 3]
            return False
        v = vv
    return True

@utils.timeit
def part1(fname):
    res = 0
    for line in utils.f2lines(fname):
        if check(utils.s2ns(line)):
            res += 1
    return res

def do1():
    assert 2 == part1(ftest)
    assert 564 == part1(finput)

def check_part2(ns):
    for n in range(len(ns)):
        if check(ns[:n] + ns[n+1:]): # sublist without element @ position n
            return True
    return False

@utils.timeit
def part2(fname):
    res = 0
    for line in utils.f2lines(fname):
         ns = utils.s2ns(line)
         if check(ns) or check_part2(ns):
             res += 1
    return res

def do2():
    assert 4 == part2(ftest)
    assert 604 == part2(finput)
