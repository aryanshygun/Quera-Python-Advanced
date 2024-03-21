# https://quera.org/college/3078/chapter/8684/lesson/29941/?comments_page=1&comments_filter=ALL&submissions_page=1

x, y = map(int, input().split())
b = int(input())
blist = []
for i in range(b):
    xx, yy = map(int, input().split())
    blist.append([xx, yy])
    
def value(i, j, blist):
    if [i, j] in blist:
        return '*'
    else:
        # x = 0
        # return 'n'
        x = 0
        pos = [-1, 0, 1]

        for u in pos:
            for k in pos:
                if u != 0 or j != 0:
                    if [i + u, j + k] in blist:
                        x +=1
        return x

for i in range(1, 1 + x):
    for j in range(1, 1 + y):
        print(value(i, j, blist), end=' ')
    print()
    
    
'''
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
    
'''