class Employee:
    raise_value = 10

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = first + last + "@company.com"
    
    def raise_pay(self):
        self.pay = self.pay + self.raise_value
    
    @classmethod
    def to_obj(cls, emp_str):
        first, last, pay = emp_str.split('_')
        return cls(first, last, int(pay))
    
    @classmethod
    def change_raise_value(cls, new_value):
        cls.raise_value = new_value
    
emp1 = Employee("arsene", "lupin", 30)
emp2_str = "matt_blanc_30"
emp2 = Employee.to_obj(emp2_str)

Employee.change_raise_value(40)
emp2.raise_pay()
print(emp2.pay)