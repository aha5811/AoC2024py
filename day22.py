import utils
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day22_test.txt')
finput = os.path.join(dir, 'day22_input.txt')

def mix(n: int, v: int) -> int:
    return n ^ v

def prune(n: int) -> int:
    return n % 16777216

def next(s: int) -> int:
    s = prune(mix(s, s * 64))
    s = prune(mix(s, s // 32))
    return prune(mix(s, s * 2048))

@utils.timeit
def part1(fname):
    res = 0

    for line in utils.f2lines(fname):
        s = int(line)
        for _ in range(2000):
            s = next(s)
        res += s

    return res

def do1():
    assert 37327623 == part1(ftest)
    assert 18261820068 == part1(finput)
