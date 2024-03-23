# https://quera.org/college/3078/chapter/9362/lesson/103385/?comments_page=1&comments_filter=ALL&submissions_page=1

def fruits(tuple_of_fruits):
    xlist = []
    xdict = {}
    for i in tuple_of_fruits:
        if i['shape'] == 'sphere' and 300 <= i['mass'] <= 600 and 100 <= i['volume'] <= 500:
            xlist.append(i['name'])
    for j in xlist:
        if j in xdict:
            xdict[j] +=1
        else:
            xdict[j] = 1
    return xdict
