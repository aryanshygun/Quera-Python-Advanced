# https://quera.org/college/3078/chapter/9362/lesson/103389/?comments_page=2&comments_filter=ALL&submissions_page=1
import re
def words_check(text):
    xlist = list(re.split(' |\n', text))
    xlist.sort()
    pattern = r'[a-zA-Z]'
    xdict = {}
    ylist = []
    
    for i in xlist:
        if len(re.findall(pattern, i)) > len(i) / 2:
            for j in i:
                if j not in re.findall(pattern, i):
                    i = i.replace(j, '')
            ylist.append(i)
    for i in range(len(ylist)):
        ylist[i] = ylist[i].title()
    for i in ylist:
        if i in xdict:
            xdict[i] += 1         
        else:
            xdict[i] = 1


    return xdict

