class User:
    def setAge(self, age):
        if age >= 0:
            self.age = age
        else:
            raise Exception('Возраст должен быть больше 0')


class Employee(User):
    def setAge(self, age):
        if age < 0:
            raise Exception('Возраст должен быть больше 0')
        elif age > 120:
            raise Exception('Возраст должен быть меньше 120')
        super().setAge(age) 


