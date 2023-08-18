class UniversityStaff:
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")


class Academic(UniversityStaff):
    def __init__(self, name, employee_id, department, title):
        super().__init__(name, employee_id, department)
        self.title = title

    def print_academic_info(self):
        print(f"Academic Title: {self.title}")


class TeachingStaff(Academic):
    def __init__(self, name, employee_id, department, title, courses_taught, role):
        super(Academic, self).__init__(name, employee_id, department, title)
        self.courses_taught = courses_taught
        self.role = role

    def print_courses(self):
        print("Courses Taught:")
        for course in self.courses_taught:
            print(course)


class AdministrativeStaff(UniversityStaff):
    def __init__(self, name, employee_id, department, role):
        super().__init__(name, employee_id, department)
        self.role = role

    def print_admin_info(self):
        print(f"Administrative Role: {self.role}")


class Registrar(AdministrativeStaff):
    def __init__(self, name, employee_id, department, role, office):
        super().__init__(name, employee_id, department, role)
        self.office = office

    def print_info(self):
        super().print_info()
        self.print_admin_info()
        print(f"Office: {self.office}")


class TeachingAdministrator(TeachingStaff, AdministrativeStaff):
    def __init__(self, name, employee_id, department, title, courses_taught, role):
        super().__init__(name, employee_id, department, title, courses_taught, role)
        self.title = title

    def print_info(self):
        super().print_info()
        self.print_admin_info()
        self.print_academic_info()
        self.print_courses()


