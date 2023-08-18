import school

Purdue = school.University("Purdue University", "West Lafayette")
dept = school.Department("Purdue University", "West Lafayette", "Computer Engineer", "Dr. Tuninetti")

print("University Information:")
Purdue.print_info()
print("\nDepartment Information:")
dept.print_department_info()
