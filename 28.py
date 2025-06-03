class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    def display_info(self):
        print(f"Username: {self.username}, Email: {self.email}")
class Employee(User):
    def __init__(self, username, email, salary):
        super().__init__(username, email) 
        self.salary = salary

    def display_info(self):
        super().display_info()  
        print(f"Salary: ${self.salary}")


if __name__ == "__main__":
    employee = Employee("Alice", "alice@example.com", 70000)
    employee.display_info()

