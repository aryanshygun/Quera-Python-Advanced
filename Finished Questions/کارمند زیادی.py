# https://quera.org/college/3078/chapter/8684/lesson/30096/?comments_page=1&comments_filter=ALL&submissions_page=1

n = int(input())
xdict = {}
for i in range(n):
    a, b = map(str, input().split())
    if a in xdict:
        xdict[a] += 1
    else:
        xdict[a] = 1
print(max(xdict.values()))