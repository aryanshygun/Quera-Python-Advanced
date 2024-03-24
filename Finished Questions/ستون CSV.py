# https://quera.org/college/3078/chapter/8685/lesson/56078/?comments_page=1&comments_filter=ALL&submissions_page=1
def process(path):
    with open(path, 'r') as f:
        xlist = []
        for row in f.readlines():
            row = row.rstrip().split(',')
            x = 0
            for i in range(len(row)):
                row[i] = int(row[i])
                x += row[i]
            row.append(x)
            roow = ', '.join(str(i) for i in row)
            xlist.append(roow)
    # print(xlist)
    with open('ans.csv', 'w') as g:
        for i in xlist:
            g.write(i + '\n')


process('Quera-College/Advanced Python Programming and Object-Oriented Thinking/sotoone_csv/test1_sample.csv')