class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def capitalize_first_letter(self, string):
        if string:
            return string[0].upper() + string[1:]
        return string

    def initials(self):
        first_initial = self.capitalize_first_letter(self.name)
        second_initial = self.capitalize_first_letter(self.surname)
        return f"{first_initial[0]}.{second_initial[0]}."

student = Student("ivan", "ivanov")
print(student.initials())

