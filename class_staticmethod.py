import datetime

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = first + last + "@company.com"

    def fullname(self):
        return self.first + " " + self.last
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:    #   mon = 0, sun = 6
            return False
        return True
    
emp1 = Employee("arsene", "lupin", 30)
emp2 = Employee("matt", "blanc", 30)

print(Employee.is_workday(datetime.date(2020, 10, 31)))
print(Employee.is_workday(datetime.date.today()))