# https://quera.org/college/3078/chapter/8684/lesson/31749/?comments_page=1&comments_filter=ALL&submissions_page=1


def calc(xlist):
    avg = sum(xlist) / len(xlist)
    mid = 0
    if len(xlist) % 2 != 0:
        mid = xlist[(len(xlist) // 2)]
    else:
        mid = (xlist[(len(xlist) // 2) - 1] + xlist[(len(xlist) // 2)]) / 2
    xmax = max(xlist)
    x = (avg, mid, xmax)
    return x
