class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
class Employee(User):
    def __init__(self, username, email, age, salary):
        super().__init__(username, email)
        self.age = age
        self.salary = salary
    def get_age(self):
        return self.age
    def get_salary(self):
        return self.salary
employee = Employee("john_doe", "john@example.com", 30, 50000)
print(f"Username: {employee.username}, Email: {employee.email}, Age: {employee.get_age()}, Salary: {employee.get_salary()}")
