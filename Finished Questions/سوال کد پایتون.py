# https://quera.org/college/3078/chapter/8685/lesson/29759/?comments_page=2&comments_filter=ALL&submissions_page=1

def solve(path)
    with open(f'{path}', 'r') as f:
        x = 0
        while (line := f.readline()) != '':
            line = line.strip()
        # print(line[0])
            if len(line) != 0:
                if line[0] != '#':
                    x += 1
    return x