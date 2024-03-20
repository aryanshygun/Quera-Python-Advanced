x, y = map(int, input().split())
n = int(input())
dots = []
for i in range(n):
    a, b = map(int, input().split())
    dots.append([a - 1, b - 1])
# print(dots)



# x, y = 4, 3
# n = 5
# dots = [[0, 0], [0, 2], [2, 1], [3, 1], [3, 2]]


for i in range(x):
    for j in range(y):
        if [i, j] in dots:
            print('*', end=' ')
        else:
            x = 0
            pos = [-1, 0, 1]
            for a in pos:
                for b in pos:
                    if [i + a, j + b] in dots:
                        x += 1
            
            print(x, end=' ')
    print()
    