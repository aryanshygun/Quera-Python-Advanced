# https://quera.org/college/3078/chapter/8684/lesson/30098/?comments_page=1&comments_filter=ALL&submissions_page=1

print(*(x for x in sorted(list(map(int, input().split()))[5::6]) if x % 2 == 0 and x % 3 == 0))

