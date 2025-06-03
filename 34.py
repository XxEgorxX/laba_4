class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __get_user_info(self):
        return f"Username: {self.username}, Email: {self.email}"

class Employee(User):
    def __init__(self, username, email, age, salary):
        super().__init__(username, email)
        self.age = age
        self.salary = salary

    def get_age(self):
        return self.age

    def get_salary(self):
        return self.salary

    def get_employee_info(self):
        user_info = self._User __get_user_info()
        return f"{user_info}, Age: {self.get_age()}, Salary: {self.get_salary()}"

employee = Employee("john_doe", "john@example.com", 30, 50000)
print(employee.get_employee_info())
