import utils
from collections import Counter
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day01_test.txt')
finput = os.path.join(dir, 'day01_input.txt')

def read(fname):
    l1, l2 = [], []
    for line in utils.f2lines(fname):
        n2 = utils.s2ns(line)
        l1.append(n2[0])
        l2.append(n2[1])
    return (l1, l2)

@utils.timeit
def part1(fname):
    res = 0
    l1, l2 = read(fname)
    l1.sort()
    l2.sort()
    for (n1, n2) in zip(l1, l2):
        res += abs(n1 - n2)
    return res

def do1():
    assert 11 == part1(ftest)
    assert 2057374 == part1(finput)

@utils.timeit
def part2(fname):
    res = 0
    l1, l2 = read(fname)
    c1, c2 = Counter(l1), Counter(l2)
    for n in c1:
        res += n * c1[n] * c2[n]
    return res

def do2():
    assert 31 == part2(ftest)
    assert 23177084 == part2(finput)
