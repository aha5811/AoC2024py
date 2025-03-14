import utils
import os.path
import functools
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day09_test.txt')
finput = os.path.join(dir, 'day09_input.txt')

class Block:
    def __init__(self, bid, start, size):
        self.bid = bid
        self.start = start
        self.size = size
        self.end = self.start + self.size - 1

    def __str__(self):
        return str(self.bid) + ':' + str(self.start) + '-' + str(self.end) + '(' + str(self.size) + ')'

    def checksum(self):
        res = 0
        for p in range(self.start, self.end + 1):
            res += self.bid * p
        return res


def read(fname):
    blocks = []

    s = utils.f2lines(fname)[0]
    is_file = True
    bid = 0
    p = 0
    for ch in s:
        n = int(ch)
        blocks.append(Block(bid if is_file else None, p, n))
        if is_file:
            bid += 1
        p += n
        is_file = not is_file

    return blocks

class GTFO(Exception):
    pass

@utils.timeit
def part1(fname):
    blocks = read(fname)

    dst_idx = 0
    src_idx = len(blocks) - 1

    moved_single_blocks = []

    try:
        while True:
            # find the next file block where we move from
            src_block = blocks[src_idx]
            while src_block.bid is None or src_block.size == 0:
                src_idx -= 1
                src_block = blocks[src_idx]

            while src_block.size > 0:

                # find the next space block where to move to
                dst_block = blocks[dst_idx]
                while dst_block.bid is not None or dst_block.size == 0:
                    dst_idx += 1
                    if dst_idx >= src_idx:
                        raise GTFO
                    dst_block = blocks[dst_idx]

                moved_single_blocks.append(Block(src_block.bid, dst_block.start, 1))
                src_block.size -= 1
                src_block.end -= 1
                dst_block.start += 1
                dst_block.size -= 1
    except GTFO:
        pass

    blocks = list(filter(lambda b: b.bid is not None and b.size > 0, blocks))
    blocks += moved_single_blocks
    blocks.sort(key=functools.cmp_to_key(lambda b1, b2: b1.start - b2.start)) # actually this is not needed

    res = 0
    for b in blocks:
        res += b.checksum()
    return res

def do1():
    assert 1928 == part1(ftest)
    assert 6283170117911 == part1(finput)

@utils.timeit
def part2(fname):
    blocks = read(fname)

    for f in filter(lambda b : b.bid is not None, reversed(blocks)):
        ss = None
        for s in filter(lambda b : b.bid is None, blocks):
            if s.start > f.start:
                break
            if s.size >= f.size:
                ss = s
                break
        if ss:
            f.start = ss.start
            f.end = f.start + f.size - 1
            ss.size -= f.size
            ss.start += f.size

    res = 0
    for b in blocks:
        if b.bid is not None:
            res += b.checksum()
    return res

def do2():
    assert 2858 == part2(ftest)
    assert 6307653242596 == part2(finput)
