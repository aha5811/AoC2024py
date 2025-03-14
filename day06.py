import utils
import maps
from maps import Map
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day06_test.txt')
finput = os.path.join(dir, 'day06_input.txt')

@utils.timeit
def part1(fname):

    m = Map(fname)

    ds = [ maps.dN, maps.dE, maps.dS, maps.dW ]
    def turn(di):
        return (di + 1) % len(ds)

    gp = m.findAll('^')[0] # guard position
    gdi = 0 # guard direction index
    v = 'x' # visited marker

    while m.get(gp.x, gp.y) is not None:
        d = ds[gdi]
        xx = gp.x + d[0]
        yy = gp.y + d[1]
        if m.get(xx, yy) is '#':
            gdi = turn(gdi)
        else:
            gp.x = xx
            gp.y = yy
            m.set(gp.x, gp.y, v) # visited

    return len(m.findAll(v)) # count visited

def do1():
    assert 41 == part1(ftest)
    assert 4656 == part1(finput)
