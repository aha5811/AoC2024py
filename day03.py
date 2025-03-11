import utils
import re
import os.path
dir = os.path.dirname(__file__)
ftest1 = os.path.join(dir, 'day03_test.txt')
ftest2 = os.path.join(dir, 'day03_2_test.txt')
finput = os.path.join(dir, 'day03_input.txt')

reMul = "mul\\((\\d+),(\\d+)\\)"

def mul(m):
    return int(m[0]) * int(m[1])

def getMul1(s):
    res = 0
    for m in re.findall(reMul, s):
        res += mul(m)
    return res

def part(mulF, fname):
    s = ""
    for line in utils.f2lines(fname):
        s += line
    return mulF(s)

@utils.timeit
def part1(fname):
    return part(getMul1, fname)

def do1():
    print(161 == part1(ftest1))
    print(part1(finput))
    #174960292

re2 = reMul + "|(do(?:n't)?)\\(\\)"

def getMul2(s):
    res = 0
    doMul = True
    for m in re.findall(re2, s):
        if m[2] == "do":
            doMul = True
        elif m[2] == "don't":
            doMul = False
        elif doMul:
            res += mul(m)
    return res    

@utils.timeit
def part2(fname):
    return part(getMul2, fname)

def do2():
    print(48 == part2(ftest2))
    print(part2(finput))
    #56275602
