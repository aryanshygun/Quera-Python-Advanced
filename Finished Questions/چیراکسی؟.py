# https://quera.org/college/3078/chapter/8773/lesson/32622/?submissions_page=1&comments_page=2&comments_filter=ALL

class ExceptionProxy(Exception):
    def __init__(self, msg, function):
        self.msg = msg
        self.function = function
    
def transform_exceptions(func_ls):
    new_func_ls = []  # Create a new list to store modified elements
    for func in func_ls:
        try:
            func()
            new_func_ls.append(ExceptionProxy('ok!', func))
        except Exception as e:
            new_func_ls.append(ExceptionProxy(str(e), func))
    return new_func_ls
