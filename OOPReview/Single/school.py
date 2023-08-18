class University:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def print_info(self):
        print(f"University Name: {self.name}")
        print(f"Location: {self.location}")


class Department(University):
    def __init__(self, name, location, department_name, head):
        super().__init__(name, location)
        self.department_name = department_name
        self.head = head

    def print_department_info(self):
        self.print_info() 
        print(f"Department Name: {self.department_name}")
        print(f"Department Head: {self.head}")
