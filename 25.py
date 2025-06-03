class Employee:
    def __init__(self, name, salary):
        """Инициализация работника с именем и зарплатой."""
        self.name = name
        self.salary = salary


class EmployeesCollection:
    def __init__(self):
        """Инициализация коллекции работников."""
        self.employees = []

    def add_employee(self, employee):
        """Добавляет нового работника в коллекцию."""
        self.employees.append(employee)

    def display_employees(self):
        """Выводит всех работников."""
        if not self.employees:
            print("No employees in the collection.")
            return
        for employee in self.employees:
            print(f"Name: {employee.name}, Salary: ${employee.salary}")

    def total_salary(self):
        """Возвращает суммарную зарплату всех работников."""
        return sum(employee.salary for employee in self.employees)

    def average_salary(self):
        """Возвращает среднюю зарплату всех работников."""
        if len(self.employees) == 0:
            return 0
        return self.total_salary() / len(self.employees)


if __name__ == "__main__":

    employees_collection = EmployeesCollection()

    employees_collection.add_employee(Employee("Alice", 70000))
    employees_collection.add_employee(Employee("Bob", 60000))
    employees_collection.add_employee(Employee("Charlie", 80000))
    employees_collection.add_employee(Employee("Diana", 75000))


    print("Employees:")
    employees_collection.display_employees()


    total = employees_collection.total_salary()
    print(f"\nTotal Salary: ${total}")


    average = employees_collection.average_salary()
    print(f"Average Salary: ${average:.2f}")
