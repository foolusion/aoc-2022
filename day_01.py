def part1(elves):
    return max(sum(x) for x in elves)


def part2(elves):
    return sum(sorted(sum(x) for x in elves)[-3:])


def main():
    with open('day_01.in', 'r') as f:
        lines = [line.strip() for line in f]
    
    elves = []
    elf = []
    for l in lines:
        if l == '':
            elves.append(elf)
            elf = []
            continue
        elf.append(int(l))
    
    print(f'{part1(elves)}')
    print(f'{part2(elves)}')
    
    
if __name__ == '__main__':
    main()
