class Employee:
    raise_value = 10

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    def raise_pay(self):
        self.pay = self.pay + self.raise_value

    def fullname(self):
        return self.first + " " + self.last

class Developer(Employee):
    raise_value = 20

    def __init__(self, first, last, pay, role):
        super().__init__(first, last, pay)
        self.role = role

class Manager(Employee):
    def __init__(self, first, last, pay, employees):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def del_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname())
    
dev1 = Developer("arsene", "lupin", 30, "frontend")
dev2 = Developer("matt", "leblanc", 30, "backend")
mgr1 = Manager("exfirst", "exlast", 30, [])

dev1.raise_pay()
mgr1.raise_pay()
print(dev1.pay)
print(mgr1.pay)

mgr1.print_emps()
mgr1.add_emp(dev1)
mgr1.add_emp(dev2)
mgr1.print_emps()
mgr1.del_emp(dev1)
mgr1.print_emps()