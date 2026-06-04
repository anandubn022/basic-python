class Employee:
    raise_value = 10
    no_of_employee = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.no_of_employee = Employee.no_of_employee + 1
        
    def raise_pay(self):
        self.pay = self.pay + self.raise_value
    
emp1 = Employee("arsene", "lupin", 30)
emp2 = Employee("matt", "leblanc", 30)

Employee.raise_value = 20
emp1.raise_pay()
emp2.raise_pay()
print(emp1.pay)
print(emp2.pay)

emp1.raise_value = 30
emp1.raise_pay()
emp2.raise_pay()
print(emp1.pay)
print(emp2.pay)

print(f"no of employee {Employee.no_of_employee}")