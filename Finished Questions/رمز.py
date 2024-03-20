# https://quera.org/college/3078/chapter/8408/lesson/29921/?comments_page=1&comments_filter=ALL&submissions_page=1

n = int(input())
m = input()
ans = 0
for i in m:
    x = input()
    moves = x.find(i)
    ans += min(moves, 9 - moves)
print(ans)




'''

n = int(input())
mkey = str(input())
mlist = [ input() for i in range(n)]
whole_moves = 0
for i in range(len(mlist)):
    x = 0
    for j in range(len(mlist[i])):
        if mkey[i] != mlist[i][j]:
            x += 1
        else:
            break
    y = 1
    for j in range(1, len(mlist[i])):
        if mkey[i] != mlist[i][-j]:
            y += 1
        else:
            break
    whole_moves += min(x, y)

print(whole_moves)

'''
