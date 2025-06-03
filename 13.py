class Employee:
    def __init__(self, name, salary, age):
        self.__name = name    
        self.__salary = salary  
        self.__age = age 

    def get_employee_data(self):
        return f"Name: {self.__name}, Salary: {self.__salary}, Age: {self.__age}"


