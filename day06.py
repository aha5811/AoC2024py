import utils
import maps
from maps import Map, Pos
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day06_test.txt')
finput = os.path.join(dir, 'day06_input.txt')

@utils.timeit
def part1(fname):

    m = Map(fname)

    ds = [ maps.dN, maps.dE, maps.dS, maps.dW ] # directions in turn order
    def turn(di):
        return (di + 1) % len(ds)

    gp: Pos = m.find_all('^')[0] # guard position Pos
    gdi = 0 # guard direction index
    v = 'x' # visited marker

    while m.get(gp.x, gp.y) is not None:
        d = ds[gdi] # direction

        # next position
        xx = gp.x + d[0]
        yy = gp.y + d[1]

        if m.get(xx, yy) == '#': # bonk -> turn
            gdi = turn(gdi)
        else:
            gp.x, gp.y = xx, yy # change guard position
            m.set(gp.x, gp.y, v) # visited

    return len(m.find_all(v)) # count visited

def do1():
    assert 41 == part1(ftest)
    assert 4656 == part1(finput)
