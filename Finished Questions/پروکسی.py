# https://quera.org/college/3078/chapter/9151/lesson/31894/?comments_page=1&comments_filter=ALL&submissions_page=1

class Proxy:
    def __init__(self, obj):
        self.last_invoked = ''
        self.calls = {}
        self._obj = obj

    def __getattr__(self, attr):
        if attr not in dir(self._obj):
            raise Exception('No Such Method')
        
        if attr not in self.calls.keys():
            self.calls[attr] = 1
        else:
            self.calls[attr] += 1
        
        self.last_invoked = attr
        return getattr(self._obj, attr)
        
        
        
        
        
        
        
    def last_invoked_method(self):
        if self.last_invoked == '':
            raise Exception('No Method Is Invoked')
        else:
            return self.last_invoked

    def count_of_calls(self, method_name):
        if method_name in self.calls.keys():
            return self.calls[method_name]
        return 0
        
    def was_called(self, method_name):
        if method_name in self.calls.keys():
            if self.calls[method_name] > 0: return True
        return False
 

   
class Radio():   
    def __init__(self):        
        self._channel = None        
        self.is_on = False        
        self.volume = 0        

    def get_channel(self):        
        return self._channel    

    def set_channel(self, value):        
        self._channel = value        

    def power(self):        
        self.is_on = not self.is_on