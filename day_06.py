def part_1(s):
    for i in range(len(s)-4):
        if len(set(s[i:i+4])) == 4:
            print(s[i:i+4])
            return i + 4
    return -1


def part_2(s):
    for i in range(len(s)-14):
        if len(set(s[i:i+14])) == 14:
            print(s[i:i+14])
            return i + 14
    return -1


def main():
    with open('day_06.in') as f:
        s = f.readline()
    print(f'{part_1(s)}')
    print(f'{part_2(s)}')


if __name__ == '__main__':
    main()
