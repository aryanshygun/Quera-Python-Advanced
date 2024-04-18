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
        s = 0
        for it in Person.instances:
            s += it.calc()
        return s


    def get_job(self):
        return self.job
    
    def upgrade(self):
        self.level += 1
    
