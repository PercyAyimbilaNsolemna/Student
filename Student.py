class Student:
    def __init__(self, name=None, studentID=None, courseList=None):
        self.name = name
        self.studentID = studentID
        self.courseList = courseList

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