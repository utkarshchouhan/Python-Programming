# Python Object-Oriented Programming

class Employee:

    a = 1000

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullName(self):
        fullName =  self.first + self.last
        return fullName

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)


emp1 = Employee("Utkarsh",'Chouhan', 50000)
emp2 = Employee("Akarsh","Chouhan", 50000)

print(emp1.apply_raise())
print(Employee.fullName(emp1))
print(emp2.fullName())
print(emp1.a)