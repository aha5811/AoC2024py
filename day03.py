import utils
import re
import profile

ftest1 = 'E:/25_aoc_py/day03_test.txt'
ftest2 = 'E:/25_aoc_py/day03_2_test.txt'
finput = 'E:/25_aoc_py/day03_input.txt'

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

def part1(fname):
    return part(getMul1, fname)

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

def part2(fname):
    return part(getMul2, fname)

print(48 == part2(ftest2))
print(part2(finput))
#56275602

profile.run("part2(finput)")
