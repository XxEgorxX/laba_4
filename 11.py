```python
class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

employee = Employee("Alex", "Smith", 50000)
print(employee.name)  
print(employee.surname) 
print(employee.salary)
```