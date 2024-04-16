# https://quera.org/college/3078/chapter/8773/lesson/29594/?comments_page=2&comments_filter=ALL&submissions_page=1

import math

class Person:
    instances = []

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.level = 1
        self.job = ''
        self.work_place = None
        Person.instances.append(self)

    def do_level(self, income) -> None:
        return income * math.sqrt(self.level * self.work_place.level)
    
    def calc_income(self):
        pass
    
    def calc_life_cost(self):
        pass
    
    def calc(self):
        return self.do_level(self.calc_income()) - self.calc_life_cost()
    
    @staticmethod
    def calc_all():
        
    


    def get_job(self):
        return self.job
    
    def upgrade(self):
        self.level += 1
    
