class UniversityStaff:
    def __init__(self, name, age, employee_id, department):
        self.name = name
        self.age = age
        self.employee_id = employee_id
        self.department = department

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"Employee ID: {self.employee_id}, Department: {self.department}")


class Academic(UniversityStaff):
    def __init__(self, name, age, employee_id, department, title):
        super().__init__(name, age, employee_id, department)
        self.title = title

    def print_academic_info(self):
        print(f"Title: {self.title}")


class Faculty(Academic):
    def __init__(self, name, age, employee_id, department, title, research_interest):
        super().__init__(name, age, employee_id, department, title)
        self.research_interest = research_interest

    def print_info(self):
        super().print_info()
        self.print_academic_info()
        print(f"Research Interest: {self.research_interest}")



