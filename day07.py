from collections.abc import Callable

import utils
import math
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day07_test.txt')
finput = os.path.join(dir, 'day07_input.txt')

def add(n1, n2): return n1 + n2
def mult(n1, n2): return n1 * n2

def solveable(t: int, n: int, ns: list[int], fs: list[Callable]) -> bool:
    """
    :param t: target
    :param n: current result
    :param ns: numbers to process
    :param fs: functions for reduction
    """
    if n > t:
        return False # can't be solved anymore
    if not ns:
        return n == t # no more numbers
    for f in fs:
        """
        recursion
        next n = current n func first of ns
        next ns = current ns without first element 
        """
        if solveable(t, f(n, ns[0]), ns[1:], fs):
            return True
    return False

def part(fname, fs):
    res = 0

    for line in utils.f2lines(fname):
        # 7290: 6 8 6 15
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
