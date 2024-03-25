class Drug:
    def __init__(self, name, amount, price) -> None:
        self.name = name
        self.amount = amount
        self.price = price
        
class Pharmacy:
       
    def __init__(self, name) -> None:
        self.name = name
        self.drugs = []
        self.employees = []
    
    def add_drug(self, drug):
        self.drugs.append((drug.name, drug.amount, drug.price))
        
    
    def add_employee(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        xdict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        self.employees.append(xdict)
 
    
    def total_value(self):
        x = 0
        for i in self.drugs:
            a, b = i.amount, i.price
            x += a * b
        return x
    
    def employees_summary(self):
        x = 'Employees:\n'
        for i in range(len(self.employees)):
            z = i + 1
            a = self.employees[i]["first_name"].title()
            b = self.employees[i]["last_name"].title()
            c = self.employees[i]["age"]
            y = f'The employee number {z} is {a} {b} who is {c} years old.\n'
            x = x + y
        return x