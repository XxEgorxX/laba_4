class User:
    def __init__(self, username, email):
        """Инициализация пользователя с именем и email."""
        self.username = username
        self.email = email

    def display_info(self):
        """Выводит информацию о пользователе."""
        print(f"Username: {self.username}, Email: {self.email}")


class Employee(User):
    def __init__(self, username, email, salary):
        """Инициализация работника с именем, email и зарплатой."""
        super().__init__(username, email)  # Вызов конструктора родительского класса
        self.salary = salary

    def display_info(self):
        super().display_info()  
        print(f"Salary: ${self.salary}")



if __name__ == "__main__":

    employee = Employee("Alice", "alice@example.com", 70000)


    print("Displaying employee information:")
    employee.display_info()

    print("\nTesting inherited method from User:")
    user_info = employee.display_info()  
