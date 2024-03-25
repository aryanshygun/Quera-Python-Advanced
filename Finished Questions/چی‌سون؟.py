# https://quera.org/college/3078/chapter/8685/lesson/31760/?comments_page=1&comments_filter=ALL&submissions_page=1
import json

n = int(input())
int_list = {}
int_dict = {}
ans=[]
for i in range(n):
    raw_input = input()
    if 'print' not in raw_input:
        intstr = list(raw_input.split(' := '))
        if isinstance(json.loads(intstr[1]), dict):
            int_dict[intstr[0]] = json.loads(intstr[1])

        elif isinstance(json.loads(intstr[1]), list):
            int_list[intstr[0]] = json.loads(intstr[1])
    
    else:
        prnt, x = raw_input.split()
        xkey, xval = x.split('[')
        xval = xval[:-1]
        if xval.startswith('"') and xval.endswith('"'):
            xval = xval[1:-1]
            ans.append(int_dict[xkey][xval])
        else:
            xval = int(xval)
            ans.append(int_list[xkey][xval])
for i in ans:
    print(i)