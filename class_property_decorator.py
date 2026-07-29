class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    # treat method as attribute
    @property
    def fullname(self):
        return self.first + " " + self.last
    
    @fullname.setter
    def fullname(self, str1):
        first, last = str1.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
    
    @property
    def mail(self):
        return self.first + self.last + "@company.com"
    
emp1 = Employee("arsene", "lupin", 30)

emp1.first = "joe"
print(emp1.first)
print(emp1.fullname)
print(emp1.mail)

emp1.fullname = "arsene lupin"
print(emp1.first)
print(emp1.fullname)
print(emp1.mail)

del emp1.fullname
print(emp1.first)
