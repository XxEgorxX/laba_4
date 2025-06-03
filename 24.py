class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employees = [
    Employee("Alice", 70000),
    Employee("Bob", 60000),
    Employee("Charlie", 80000),
    Employee("Diana", 75000)
]


for employee in employees:
    print(f"Name: {employee.name}, Salary: ${employee.salary}")
