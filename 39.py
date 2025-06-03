class User:
    def __init__(self, name=None):
        self._name = name
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def display_info(self):
        return f":User  {self._name}"
class Employee(User):
    def __init__(self, name=None, employee_id=None):
        super().__init__(name)
        self.employee_id = employee_id
    def set_employee_id(self, employee_id):
        self.employee_id = employee_id
    def get_employee_id(self):
        return self.employee_id
    def display_info(self):
        return f"Employee: {self._name}, ID: {self.employee_id}"
class Programmer(Employee):
    def __init__(self, name=None, employee_id=None, programming_language=None):
        super().__init__(name, employee_id)
        self.programming_language = programming_language
    def set_programming_language(self, language):
        self.programming_language = language
    def get_programming_language(self):
        return self.programming_language
    def display_info(self):
        return f"Programmer: {self._name}, ID: {self.employee_id}, Language: {self.programming_language}"
class Designer(Employee):
    def __init__(self, name=None, employee_id=None, design_tool=None):
        super().__init__(name, employee_id)
        self.design_tool = design_tool

    def set_design_tool(self, tool):
        self.design_tool = tool

    def get_design_tool(self):
        return self.design_tool

    def display_info(self):
        return f"Designer: {self._name}, ID: {self.employee_id}, Tool: {self.design_tool}"
