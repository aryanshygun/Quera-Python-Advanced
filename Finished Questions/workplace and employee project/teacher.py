# YOUR IMPORTS GOES HERE
import math
from person import Consts, Person

class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.job = 'teacher'

    def get_price(self):
        bp = Consts.BASE_PRICE[self.job]
        self.price = int(bp - (self.age - Consts.MIN_AGE)*Consts.AGE_MUL)
        return self.price
    
    def calc_life_cost(self):
        bc = Consts.BASE_COST[self.job]
        self.costs = int(bc + (self.age - Consts.MIN_AGE)*Consts.AGE_MUL)
        return self.costs

    def calc_income(self):
        bi = Consts.BASE_INCOME[self.job][self.work_place.get_expertise()]
        self.income = int(bi - (self.age - Consts.MIN_AGE)*Consts.AGE_MUL)
        return self.income