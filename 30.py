class User:
    def __init__(self, username, email):
        """Инициализация пользователя с именем и email."""
        self.username = username
        self.email = email

    def display_info(self):
        """Выводит информацию о пользователе."""
        return f"Username: {self.username}, Email: {self.email}"


class Employee(User):
    def __init__(self, username, email, salary, last_name):
        """Инициализация работника с именем, email, зарплатой и фамилией."""
        super().__init__(username, email)  # Вызов конструктора родительского класса
        self.salary = salary
        self.last_name = last_name


    @property
    def salary(self):
        """Геттер для зарплаты."""
        return self._salary

    @salary.setter
    def salary(self, value):
        """Сеттер для зарплаты."""
        if value < 0:
            raise ValueError("Зарплата не может быть отрицательной.")
        self._salary = value


    @property
    def username(self):
        """Геттер для имени."""
        return self._username

    @username.setter
    def username(self, value):
        """Сеттер для имени."""
        if not value:
            raise ValueError("Имя не может быть пустым.")
        self._username = value


    @property
    def last_name(self):
        """Геттер для фамилии."""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """Сеттер для фамилии."""
        if not value:
            raise ValueError("Фамилия не может быть пустой.")
        self._last_name = value

    def display_info(self):
        
        user_info = super().display_info()  
        return f"{user_info}, Last Name: {self.last_name}, Salary: ${self.salary}"



if __name__ == "__main__":
    
    employee = Employee("Alice", "alice@example.com", 70000, "Smith")

  
    print("Информация о работнике:")
    print(employee.display_info())

    employee.salary = 80000 
    employee.username = "AliceUpdated"  
    employee.last_name = "Johnson" 

    print("\nОбновленная информация о работнике:")
    print(employee.display_info())

    # Проверка, что методы работают корректно
    assert employee.salary == 80000, "Зарплата не обновилась корректно."
    assert employee.username == "AliceUpdated", "Имя не обновилось корректно."
    assert employee.last_name == "Johnson", "Фамилия не обновилась корректно."

    print("Все проверки прошли успешно!")
