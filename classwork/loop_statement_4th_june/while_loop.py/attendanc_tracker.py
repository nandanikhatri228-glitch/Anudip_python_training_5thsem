#a teacher is recording the attendance of students the strength is 30 evertime he need to insert the student present or absent .so count the total number student present as well as student absent
student_count = 0
present_student = 0
absent_student = 0

while student_count < 30:
    student_count += 1

    attendance = input("Enter attendance of student (p/a): ")

    if attendance == "p":
        present_student += 1
        print("student",student_count)
        print("Atttendance: present")

    elif attendance == "a":
        absent_student += 1
        print("student",student_count)
        print("Atttendance: absent")

print("Total students present:", present_student)
print("Total students absent:", absent_student)
