import utils
import math
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day07_test.txt')
finput = os.path.join(dir, 'day07_input.txt')

def add(n1, n2): return n1 + n2
def mult(n1, n2): return n1 * n2

def solveable(t, n, ns, fs):
    if n > t:
        return False
    if not ns:
        return True if n == t else False
    nn = ns.pop(0)
    for f in fs:
        if solveable(t, f(n, nn), ns.copy(), fs):
            return True
    return False

def part(fname, fs):
    res = 0

    for line in utils.f2lines(fname):
        ns = utils.s2is(line.replace(":", ""), " ")
        t = ns.pop(0)
        n = ns.pop(0)
        if solveable(t, n, ns, fs):
            res += t
    
    return res

@utils.timeit
def part1(fname):
    return part(fname, [add, mult])

def do1():
    assert 3749 == part1(ftest)
    assert 1399219271639 == part1(finput)

def conc(n1, n2): return int(str(n1) + str(n2))

@utils.timeit
def part2(fname):
    return part(fname, [add, mult, conc])

def do2():
    assert 11387 == part2(ftest)
    assert 275791737999003 == part2(finput)
