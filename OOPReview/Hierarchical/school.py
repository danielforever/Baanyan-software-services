class UniversityStaff:
    def __init__(self, name, age, employee_id, department):
        self.name = name
        self.age = age
        self.employee_id = employee_id
        self.department = department

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"Employee ID: {self.employee_id}, Department: {self.department}")


class Faculty(UniversityStaff):
    def __init__(self, name, age, employee_id, department, title, research_interest):
        super().__init__(name, age, employee_id, department)
        self.title = title
        self.research_interest = research_interest

    def print_info(self):
        super().print_info()
        print(f"Title: {self.title}, Research Interest: {self.research_interest}")


class AdministrativeStaff(UniversityStaff):
    def __init__(self, name, age, employee_id, department, role):
        super().__init__(name, age, employee_id, department)
        self.role = role

    def print_info(self):
        super().print_info()
        print(f"Role: {self.role}")


class JanitorialStaff(UniversityStaff):
    def __init__(self, name, age, employee_id, department, shift):
        super().__init__(name, age, employee_id, department)
        self.shift = shift

    def print_info(self):
        super().print_info()
        print(f"Shift: {self.shift}")


