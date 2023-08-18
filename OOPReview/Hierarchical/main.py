import school


professor = school.Faculty("John Doe", 45, "E123", "Computer Science", "Professor", "Machine Learning")
admin_staff = school.AdministrativeStaff("Jane Smith", 32, "A456", "Administration", "Coordinator")
janitor = school.JanitorialStaff("Mike Johnson", 50, "J789", "Facilities", "Night Shift")


professor.print_info()
print("\n")
admin_staff.print_info()
print("\n")
janitor.print_info()