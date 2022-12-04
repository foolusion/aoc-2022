def part_1(lines: list[str]):
    sacks = [(set(line[:len(line)//2]), set(line[len(line)//2:])) for line in lines]
    duplicates = []
    for sack in sacks:
        for item in sack[1]:
            if item in sack[0]:
                duplicates.append(item)
    return sum(priority(item) for item in duplicates)
    

def priority(item: str):
    if item.islower():
        return ord(item) - (97 - 1)
    return ord(item) - (65 - 26 - 1)


def part_2(lines: list[str]):
    groups = [[set(lines[i]), set(lines[i+1]), set(lines[i+2])] for i in range(0, len(lines), 3)]
    duplicates = []
    for [a, b, c] in groups:
        res = next(iter(a & b & c))
        duplicates.append(res)
    return sum(priority(item) for item in duplicates)


def main():
    with open('day_03.in') as f:
        lines = [line.strip() for line in f]
    print(f'{part_1(lines)}')
    print(f'{part_2(lines)}')


if __name__ == '__main__':
    main()
    