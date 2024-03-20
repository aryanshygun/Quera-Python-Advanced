# https://quera.org/college/3078/chapter/9362/lesson/103370/?comments_page=1&comments_filter=ALL

def calculator(n, m, ls):
    xlist = []
    for i in range(0, len(ls), m):
        xlist.append(sum(ls[i:i+m]))
    x = 0
    for i in range(len(xlist)):
        # x = 0
        if i % 2 == 0:
            x += xlist[i]
        else:
            x -= xlist[i]
    return x
            
# Local Tests
print(calculator(8, 3, [1, 2, 3, 4, 5, 6, 7, 8]))
# print(calculator(8, 1, [1, 2, 3, 4, 5, 6, 7, 8]))
