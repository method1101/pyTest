""" Learning Classes in Python """

class Employee:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname
  def greet(self):
    return f'Hello {self.fname} {self.lname}'

emp1 = Employee('John', 'Smith')
print(emp1.greet())
print(Employee.greet(emp1))
