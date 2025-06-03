class Employee:
    def __init__(self, name, salary, age):
        self.__name = name      
        self.__salary = salary  
        self.__age = age        

    def get_name(self):
        return self.__name     

    def set_name(self, name):
        self.__name = name      

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_age(self):
        return self.__age   

    def set_age(self, age):
        self.__age = age    

