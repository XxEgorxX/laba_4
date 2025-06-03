class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        return f"Username: {self.username}, Email: {self.email}"


class Employee(User):
    def __init__(self, username, email, salary, last_name, age):
        super().__init__(username, email)
        self.salary = salary
        self.last_name = last_name
        self.age = age

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Зарплата не может быть отрицательной.")
        self._salary = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Имя не может быть пустым.")
        self._username = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value:
            raise ValueError("Фамилия не может быть пустой.")
        self._last_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 18 or value > 65:
            raise ValueError("Возраст должен быть от 18 до 65 лет.")
        self._age = value

    def display_info(self):
        user_info = super().display_info()
        return f"{user_info}, Last Name: {self.last_name}, Salary: ${self.salary}, Age: {self.age}"


if __name__ == "__main__":
    employee = Employee("Alice", "alice@example.com", 70000, "Smith", 30)
    print("Информация о работнике:")
    print(employee.display_info())

    employee.salary = 80000
    employee.username = "AliceUpdated"
    employee.last_name = "Johnson"
    employee.age = 35

    print("\nОбновленная информация о работнике:")
    print(employee.display_info())

    assert employee.salary == 80000
    assert employee.username == "AliceUpdated"
    assert employee.last_name == "Johnson"
    assert employee.age == 35

    print("Все проверки прошли успешно!")
