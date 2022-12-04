def part_1(lines):
    pairs = [tuple(tuple(int(a) for a in p.split('-')) for p in line.split(',')) for line in lines]
    overlaps = []
    for (e1, e2) in pairs:
        if contains(e1, e2) or contains(e2, e1):
            overlaps.append((e1, e2))
    return len(overlaps)


def contains(e1, e2):
    return e1[0] <= e2[0] and e1[1] >= e2[1]
    

def part_2(lines):
    pairs = [tuple(tuple(int(a) for a in p.split('-')) for p in line.split(',')) for line in lines]
    overlaps = []
    for (e1, e2) in pairs:
        if not(separate(e1, e2)):
            overlaps.append((e1, e2))
    return len(overlaps)
    

def separate(e1, e2):
    return e1[1] < e2[0] or e1[0] > e2[1]


def main():
    with open('day_04.in') as f:
        lines = [line.strip() for line in f]
    print(f'{part_1(lines)}')
    print(f'{part_2(lines)}')


if __name__ == '__main__':
    main()
