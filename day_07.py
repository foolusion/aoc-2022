class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = []
        self.dirs = {}
    
    def add_file(self, size, name):
        self.files.append((size, name))
    
    def add_dir(self, d):
        self.dirs[d.name] = d


def part_1(directory):
    current_dir = directory
    total = sum(f[0] for f in current_dir.files)
    child_totals = []
    children = []
    for d in current_dir.dirs.values():
        t, tlist = part_1(d)
        children += tlist
        child_totals.append(t)
    return total + sum(child_totals), [total + sum(child_totals)] + children


def to_dir_tree(lines):
    listing_files = False
    starting_dir = None
    current_dir = None
    for line in lines:
        if line.startswith('$ cd'):
            listing_files = False
            if line.endswith('..'):
                current_dir = current_dir.parent
            else:
                if current_dir is None:
                    starting_dir = Dir(line[5:])
                    current_dir = starting_dir
                else:
                    d = line[5:]
                    current_dir = current_dir.dirs[d]
        elif line.startswith('$ ls'):
            listing_files = True
        elif listing_files and line.startswith('dir'):
            d = Dir(line[4:], current_dir)
            current_dir.add_dir(d)
        elif listing_files:
            size, name = line.split()
            current_dir.add_file(int(size), name)
    return starting_dir


def main():
    with open('day_07.in') as f:
        lines = [line.strip() for line in f]
    dir_tree = to_dir_tree(lines)
    total, dir_sizes = part_1(dir_tree)
    print(sum(a for a in dir_sizes if a <= 100000))
    print(min(a for a in dir_sizes if a >= 30_000_000 - (70_000_000 - total)))


if __name__ == '__main__':
    main()
