import re
from typing import Match

"""
    [G] [R]                 [P]
    [H] [W]     [T] [P]     [H]
    [F] [T] [P] [B] [D]     [N]
[L] [T] [M] [Q] [L] [C]     [Z]
[C] [C] [N] [V] [S] [H]     [V] [G]
[G] [L] [F] [D] [M] [V] [T] [J] [H]
[M] [D] [J] [F] [F] [N] [C] [S] [F]
[Q] [R] [V] [J] [N] [R] [H] [G] [Z]
 1   2   3   4   5   6   7   8   9
"""
ORIGINAL_STACKS = [
    [ch for ch in 'QMGCL'],
    [ch for ch in 'RDLCTFHG'],
    [ch for ch in 'VJFNMTWR'],
    [ch for ch in 'JFDVQP'],
    [ch for ch in 'NFMSLBT'],
    [ch for ch in 'RNVHCDP'],
    [ch for ch in 'HCT'],
    [ch for ch in 'GSJVZNHP'],
    [ch for ch in 'ZFHG'],
]


def part_1(lines: list[tuple[int, int, int]], stacks: list[str]):
    for (c, f, t) in lines:
        f = f - 1
        t = t - 1
        for i in range(c):
            temp = stacks[f].pop()
            stacks[t].append(temp)
    return "".join(s[-1] for s in stacks)


def part_2(lines, stacks):
    for (c, f, t) in lines:
        f -= 1
        t -= 1
        stacks[t] += stacks[f][-c:]
        stacks[f] = stacks[f][0:-c]
    return "".join(s[-1] for s in stacks)


def main():
    with open('day_05.in') as f:
        lines = []
        for line in f:
            m = re.search(r'move (\d+) from (\d+) to (\d+)', line)
            a, b, c = m.groups()
            lines.append((int(a), int(b), int(c)))
    print(f'{part_1(lines, [a.copy() for a in ORIGINAL_STACKS])}')
    print(f'{part_2(lines, [a.copy() for a in ORIGINAL_STACKS])}')


if __name__ == '__main__':
    main()
