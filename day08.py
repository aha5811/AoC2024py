from itertools import count

import utils
from maps import Map, Pos
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day08_test.txt')
finput = os.path.join(dir, 'day08_input.txt')

def get_antinodes_part1(m: Map, a1: Pos, a2: Pos) -> list[Pos]:
    res = []

    dx, dy = a2.x - a1.x, a2.y - a1.y

    an1 = Pos(a2.x + dx, a2.y + dy)
    if m.get(an1.x, an1.y) is not None:
        res.append(an1)

    an2 = Pos(a1.x - dx, a1.y - dy)
    if m.get(an2.x, an2.y) is not None:
        res.append(an2)

    return res

def part(fname, get_antinodes: callable) -> int:

    m = Map(fname)

    antenna_group_symbols = m.get_symbols()
    antenna_group_symbols.remove(".")

    antinodes = set()

    for s in antenna_group_symbols:
        antennas = m.find_all(s)
        for a1 in antennas:
            for a2 in antennas:
                if a1 is not a2:
                    antinodes.update(get_antinodes(m, a1, a2))
    
    return len(antinodes)

@utils.timeit
def part1(fname):
    return part(fname, get_antinodes_part1)

def do1():
    assert 14 == part1(ftest)
    assert 259 == part1(finput)

def get_antinodes_part2(m: Map, a1: Pos, a2: Pos) -> list[Pos]:
    res = []

    dx = a2.x - a1.x
    dy = a2.y - a1.y

    def add_antinodes(a: Pos, nm: int):
        for n in count():
            x = a.x + nm * n * dx
            y = a.y + nm * n * dy
            if m.get(x, y) is None:
                break
            res.append(Pos(x, y))

    add_antinodes(a2, 1)
    add_antinodes(a1, -1)

    return res

@utils.timeit
def part2(fname):
    return part(fname, get_antinodes_part2)

def do2():
    assert 34 == part2(ftest)
    assert 927 == part2(finput)
