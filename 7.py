class User:
  name = None
  def show(self):
    print(self.name)
user = User()
user.name = 'oleg' 
user.show()

class Employee:
  name = None
  def salar(self):
    print(self.name)
    print(self.salary)
employee = Employee()
employee.name = 'alek'
employee.salary = '370$'
employee.salar()
