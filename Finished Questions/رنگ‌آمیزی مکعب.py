# https://quera.org/college/3078/chapter/9362/lesson/103382/?comments_page=2&comments_filter=ALL&submissions_page=1
def coloring(ls):
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            for k in range(len(ls[i][j])):
                ls[i][j][k] = 1

    for i in range(1, len(ls) - 1):
        for j in range(1, len(ls[i]) - 1):
            for k in range(1, len(ls[i][j]) - 1):
                ls[i][j][k] = 0
    return ls
            
'''
def coloring(ls):
    x, y, z = map(len, [ls, ls[0], ls[0][0]])
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if i == 0 or i == x - 1 or j == 0 or j == y - 1 or k == 0 or k == z - 1:
                    ls[i][j][k] = 1 
                else:
                    ls[i][j][k] = 0
                    
'''