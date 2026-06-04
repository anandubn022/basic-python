class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = first + last + "@company.com"

    def fullname(self):
        return self.first + " " + self.last
    
emp1 = Employee("arsene", "lupin", 30)
emp2_str = "matt_blanc_30"
first, last, pay = emp2_str.split('_')
emp2 = Employee(first, last, int(pay))   #   * passes values as arguments directly from function

print(emp1.fullname())
print(emp1.mail)

print(emp2.fullname())
print(emp2.mail)