d90 = [(1, 0), (0, 1), (-1, 0), (0, -1)] # W S E N
dE, dS, dW,dN = d90[0], d90[1], d90[2], d90[3]
d45 = [(1, 1), (-1, 1), (-1, -1), (1, -1)] # SE SW NW NE
dSE, dSW, dNW, dNE = d45[0], d45[1], d45[2], d45[3]
ds = d90 + d45

class Map:
    def __init__(self, fname):
        self.rows = []
        with open(fname, 'r') as f:
            for line in f:
                self.rows.append(list(line.strip()))
        self.h = len(self.rows)
        self.w = len(self.rows[0])

    def __str__(self):
        res = ""
        for row in self.rows:
            res += "".join(row)
        return res

    def get(self, x, y):
        if x < 0 or x >= self.w or y < 0 or y >= self.h:
            return None
        else:
            return self.rows[y][x]

    def set(self, x, y, c):
        if self.get(x, y) is not None:
            self.rows[y][x] = c

    def findVs(self):
        res = set(())
        for x in range(self.w):
            for y in range(self.h):
                res.add(self.get(x, y))
        return res

    def findAll(self, c):
        res = []
        for x in range(self.w):
            for y in range(self.h):
                if self.get(x, y) == c:
                    res.append(Pos(x, y))
        return res

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def __eq__(self, other):
        if isinstance(other, Pos):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash(str(self))
