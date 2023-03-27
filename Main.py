from Student import Student 

def main():
    student = Student()
    print(student)

    student.setName("Saba")
    print(f"Name: {student.getName()}")

    student.setStudentID("1123465")
    print(f"Student ID: {student.getStudentID()}")

    print("---------------- ADDS ONE COURSE -------------------")
    student.addCourse("MATH223")
    student.displayCourse()

    print("----------------- ADDS MANY COURSES -------------------")
    student.addCourse("DCIT201", "DCIT205", "CBAS210", "DCIT203", "DCIT207")
    student.displayCourse()

    print("------------------ REMOVES ONE COURSE -------------------")
    student.removeCourse("CBAS210")
    student.displayCourse()

    print("------------------ REMOVES MANY COURSES -------------------")
    student.removeCourse("CBAS210", "DCIT203", "DCIT207")
    student.displayCourse()

if __name__ == "__main__":
    main()