class Student:
    def __init__(self, name=None, studentID=None, courseList=None):
        self.name = name
        self.studentID = studentID
        self.courseList = []

    #Creates an __str__ that makes it possible to pass an object created from this class to the print function
    def __str__(self):
        return "This is a Student class"

    #Creates a getter and setter for the name attribute
    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name 

    #Creates a getter and setter for the studentID attribute
    def getStudentID(self):
        return self._studentID

    def setStudentID(self, studentID):
        self._studentID = studentID 

    #Creates a method that allows students to add courses
    def addCourse(self, *course):
        self.course = course
        for a_course in self.course:
            self.courseList.append(a_course)

    def removeCourse(self, *course):
        self.course = course
        for a_course in self.course:
            if a_course in self.courseList:
                self.courseList.remove(a_course)

    #Creates a display course method
    def displayCourse(self):
        for course in self.courseList:
            print(course)

def main():
    student = Student()
    print(student)

    student.setName("Saba")
    print(f"Name: {student.getName()}")

    student.setStudentID("1123465")
    print(f"Student ID: {student.getStudentID()}")

    student.addCourse("MATH223", "DCIT201", "DCIT205", "CBAS210", "DCIT203", "DCIT207")
    #student.displayCourse()

    student.removeCourse("CBAS210", "DCIT203", "DCIT207")
    student.displayCourse()

if __name__ == "__main__":
    main()