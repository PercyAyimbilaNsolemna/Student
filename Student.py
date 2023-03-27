class Student:
    def __init__(self, name=None, studentID=None, courseList=None):
        self.name = name
        self.studentID = studentID
        self.courseList = courseList

    #Creates an __str__ that makes it possible to pass an object created from this class to the print function
    def __str__(self):
        return "This is a Student class"

        