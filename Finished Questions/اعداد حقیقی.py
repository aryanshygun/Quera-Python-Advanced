# https://quera.org/college/3078/chapter/9362/lesson/103408/?comments_page=1&comments_filter=ALL&submissions_page=1


import re

# xlist = ['1.5e+2' ,'3.', '1.1.1', '1+e5']

def real_numbers(xlist):
    pattern = r'^\s*[+-]?(\d+(\.\d+)?)([eE][+-]?\d+)?\s*$'
    ylist = []
    for i in xlist:
        if re.match(pattern, i) != None:
            ylist.append('LEGAL')
        else:
            ylist.append('ILLEGAL')
    return ylist

print(real_numbers(['1.5e+2' ,'3.', '1.1.1', '1+e5']))