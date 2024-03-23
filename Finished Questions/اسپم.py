# https://quera.org/college/3078/chapter/9362/lesson/57071/?comments_page=1&comments_filter=ALL&submissions_page=1

import re
sender = str(input())
content = str(input())

def sender_not_digit(x):
    return not x.isdigit()

def isnt_spam(x):
    return len(re.findall('spam', x.lower())) == 0

def morestr(x):
    return len(x) - len(re.findall('[\w]', x)) <= len(x) / 2

def content_check(x):
    if isnt_spam(x) == False and morestr(x) == False:
        return False
    else:
        return True

def whole_checker(sender, content):
    if sender_not_digit(sender) == True and content_check(content) == True:
        return 'Not Spam'
    elif sender_not_digit(sender) == False and content_check(content) == True:
        return 'Invalid Sender'
    elif sender_not_digit(sender) == True and content_check(content) == False:
        return 'Invalid Content'
    elif sender_not_digit(sender) == False and content_check(content) == False:
        return 'Fully Invalid'
    
print(whole_checker(sender, content))