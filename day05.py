import utils
from utils import idx
import functools
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day05_test.txt')
finput = os.path.join(dir, 'day05_input.txt')

def is_satisfied(pages, rule):
    i1 = idx(pages, rule[0])
    i2 = idx(pages, rule[1])
    return i1 == -1 or i2 == -1 or i1 < i2

def in_order(pages, rules):
    for rule in rules:
        if not is_satisfied(pages, rule):
            return False
    return True

def read(fname):
    rules = []
    books = []
    lines = utils.f2lines(fname)
    for l in lines:
        if "|" in l:
            # 53|13
            rules.append(utils.s2is(l, "|"))
        elif "," in l:
            # 75,47,61,53,29
            books.append(utils.s2is(l, ","))
    return rules, books

def middle(os):
    return os[int(len(os) / 2)]

@utils.timeit
def part1(fname):
    rules, books = read(fname)

    res = 0
    for pages in books:
        if in_order(pages, rules):
            res += middle(pages)
    return res

def do1():
    assert 143 == part1(ftest)
    assert 4872 == part1(finput)

def sort(pages, rules):
    def compare(p1, p2):
        for rule in rules:
            if p1 == rule[0] and p2 == rule[1]:
                return -1
            elif p1 == rule[1] and p2 == rule[0]:
                return 1
        return 0  
    pages.sort(key=functools.cmp_to_key(compare))
    return pages

@utils.timeit
def part2(fname):
    rules, books = read(fname)
    
    res = 0
    for pages in books:
        if not in_order(pages, rules):
            sort(pages, rules)
            res += middle(pages)
    return res

def do2():
    assert 123 == part2(ftest)
    assert 5564 == part2(finput)
