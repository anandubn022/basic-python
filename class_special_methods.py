class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = first + last + "@company.com"

    def fullname(self):
        return self.first + " " + self.last

    # official string representation of object
    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    # human readale representaion of object
    def __str__(self):
        return f"{self.fullname()} - {self.pay}"
    
    def __add__(self, other):
        return self.pay + other.pay
    
emp1 = Employee("arsene", "lupin", 30)
emp2 = Employee("matt", "leblanc", 30)

print(emp1)
print(emp1.__repr__())
print(emp1.__str__())
print(emp1+emp2)
