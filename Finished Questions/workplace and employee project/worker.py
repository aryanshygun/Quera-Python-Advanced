# YOUR IMPORTS GOES HERE
import math
from person import Consts, Person

class Worker(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.job = 'worker'

    def get_price(self):
        bp = Consts.BASE_PRICE[self.job]
        self.price = int(bp * (Consts.MIN_AGE/self.age))
        return self.price

    def calc_life_cost(self):
        bc = Consts.BASE_COST[self.job]
        self.costs = int(bc * (self.age/Consts.MIN_AGE))
        return self.costs

    def calc_income(self):
        bi = Consts.BASE_INCOME[self.job][self.work_place.get_expertise()]
        self.income = int(bi * (Consts.MIN_AGE/self.age))
        return self.income