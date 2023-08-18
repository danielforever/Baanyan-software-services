import school


staff = school.UniversityStaff("Alex Johnson", "T123", "Computer Science")
staff.print_info()

Academic_staff = school.Academic("Alex Johnson", "T123", "Computer Science", "Associate Professor")
Academic_staff.print_academic_info()


teaching_admin = school.TeachingAdministrator(
    "Alex Johnson", "T123", "Computer Science",
    "Associate Professor", ["Data Structures", "Algorithms"], "Coordinator")

teaching_admin.print_info()