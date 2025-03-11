
def f2lines(fname):
    res = []
    with open(fname, 'r') as file:
        for line in file:
            res.append(line)
    return res

def s2ns(s):
    res = []
    for w in s.split():
        res.append(int(w))
    return res
