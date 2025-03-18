import utils
import os.path
import functools
dir = os.path.dirname(__file__)
ftest = os.path.join(dir, 'day09_test.txt')
finput = os.path.join(dir, 'day09_input.txt')

class Block:
    def __init__(self, bid, start, size):
        self.bid = bid # block id
        self.start = start
        self.size = size

    def __str__(self):
        return f'{self.bid}:{self.start}-{self.start + self.size - 1}({str(self.size)})'

    def checksum(self):
        res = 0
        for p in range(self.start, self.start + self.size):
            res += self.bid * p
        return res


def read(fname) -> list[Block]:
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
                dst_block.start += 1
                dst_block.size -= 1
    except GTFO:
        pass

    blocks = list(filter(lambda b: b.bid is not None and b.size > 0, blocks)) + moved_single_blocks

    return sum(map(lambda b: b.checksum(), blocks))

def do1():
    assert 1928 == part1(ftest)
    assert 6283170117911 == part1(finput)

@utils.timeit
def part2(fname):
    blocks = read(fname)

    spaces = list(filter(lambda b : b.bid is None, blocks)) # all spaces

    for f in filter(lambda b : b.bid is not None, reversed(blocks)): # all files from reversed
        space = None
        for s in spaces:
            if s.start > f.start:
                break
            if s.size >= f.size:
                space = s
                break
        if space:
            # move file into space
            f.start = space.start
            space.size -= f.size
            if space.size == 0:
                spaces.remove(space)
            space.start += f.size

    return sum(map(lambda b: b.checksum(), filter(lambda b: b.bid is not None, blocks)))

def do2():
    assert 2858 == part2(ftest)
    assert 6307653242596 == part2(finput)
