import utils
import profile
from collections import Counter

ftest = 'E:/25_aoc_py/day01_test.txt'
finput = 'E:/25_aoc_py/day01_input.txt'

def read(fname):
    l1, l2 = [], []
    for line in utils.f2lines(fname):
        n2 = utils.s2ns(line)
        l1.append(n2[0])
        l2.append(n2[1])
    return (l1, l2)

def part1(fname):
    res = 0
    l1, l2 = read(fname)
    l1.sort()
    l2.sort()
    for (n1, n2) in zip(l1, l2):
        res += abs(n1 - n2)
    return res

print(11 == part1(ftest))
print(part1(finput))
#2057374

def part2(fname):
    res = 0
    l1, l2 = read(fname)
    c1, c2 = Counter(l1), Counter(l2)
    for n in c1:
        res += n * c1[n] * c2[n]
    return res

print(31 == part2(ftest))
print(part2(finput))
#23177084

profile.run("part2(finput)")
