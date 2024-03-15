# https://quera.org/problemset/28948

ans = str(input())
x = []

for i in ans:
    x.append(i)

y = []
for i in range(len(x)):
    if x[0] == '=':
        # y +=1
        x.pop(0)
    else:
        break

for i in range(len(x)):
    if x[i] != '=':
        y.append(x[i])
    if x[i] == '=':
        y.pop()

for i in y:
    print(i, end='')