def part1(lines):
    lines = [[line[0], to_abc(line[1])] for line in lines]
    scores = []
    for [a, b] in lines:
        score = 0
        if b == 'A':
            score += 1
        elif b == 'B':
            score += 2
        elif b == 'C':
            score += 3
        score += match_score(b, a)
        scores.append(score)
    return sum(scores)


def to_abc(a):
    if a == 'X':
        return 'A'
    if a == 'Y':
        return 'B'
    if a == 'Z':
        return 'C'


def match_score(a, b):
    if beats(a, b):
        return 6
    if a == b:
        return 3
    else:
        return 0

 
def beats(a, b):
    return (a == 'A' and b == 'C') or (a == 'B' and b == 'A') or (a == 'C' and b == 'B')


def part2(lines):
    scores = []
    # score for [win, loss, draw]
    data = {'A': [8, 3, 4], 'B': [9, 1, 5], 'C': [7, 2, 6]}
    lines = [[line[0], to_012(line[1])] for line in lines]
    for [a, b] in lines:
        scores.append(data[a][b])
    print(scores)
    return sum(scores)


def to_012(a):
    if a == 'X':
        return 1
    if a == 'Y':
        return 2
    if a == 'Z':
        return 0

 
def main():
    with open('day_02.in') as f:
        lines = [line.strip().split(' ') for line in f]

    print(f'{part1(lines)}')
    print(f'{part2(lines)}')


if __name__ == '__main__':
    main()