import utils
import profile

ftest = 'E:/25_aoc_py/day02_test.txt'
finput = 'E:/25_aoc_py/day02_input.txt'

def xor(b1, b2):
    return (not b2 and b1) or (not b1 and b2)

def check(ns):
    v = ns[0]
    inc = ns[1] > v
    for n in range(1, len(ns)):
        v2 = ns[n]
        if xor(v2 > v, inc):
            return False
        if v2 == v or abs(v2 - v) > 3:
            return False
        v = v2
    return True

def part1(fname):
    res = 0
    for line in utils.f2lines(fname):
        if check(utils.s2ns(line)):
            res += 1
    return res

print(2 == part1(ftest))
print(part1(finput))
#564

def check2(ns):
    for n in range(len(ns)):
        if check(ns[:n] + ns[n+1:]):
            return True
    return False

def part2(fname):
    res = 0
    for line in utils.f2lines(fname):
         ns = utils.s2ns(line)
         if check(ns) or check2(ns):
             res += 1
    return res

print(4 == part2(ftest))
print(part2(finput))
#604

profile.run("part2(finput)")
