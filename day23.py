import utils
import os.path
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day23_test.txt')
finput = os.path.join(dir, 'day23_input.txt')

@utils.timeit
def part1(fname):

    nm = {} # network map
    # ab-cd, ab-ef
    # -> { ab -> [cd, ef], cd -> [ab], ef -> [ab] }
    for line in utils.f2lines(fname):
        n1, n2 = line.split('-')
        if n1 not in nm:
            nm[n1] = []
        if n2 not in nm[n1]:
            nm[n1].append(n2)
        if n2 not in nm:
            nm[n2] = []
        if n1 not in nm[n2]:
            nm[n2].append(n1)

    triples = set()

    def check_for(nm: dict, n: str):
        for n2 in nm[n]:
            for n3 in nm[n]:
                if n2 != n3:
                    # for each 2 different nodes that are connected with n
                    # if these 2 are connected then we have a triple
                    if n3 in nm[n2]:
                        triples.add(",".join(sorted([n, n2, n3])))
                        # make two triples with the same nodes the same
                        # ta <-> co <-> da -> co,da,ta
                        # co <-> ta <-> da -> co,da,ta
                        # so these are only added once to set

    for n in nm.keys():
        if n[0] == 't': # name starts with t
            check_for(nm, n)

    return len(triples)

def do1():
    assert 7 == part1(ftest)
    assert 1437 == part1(finput)
