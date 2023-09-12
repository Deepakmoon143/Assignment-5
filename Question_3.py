class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None

    def getName(self):
        return self.__name

    def setName(self, name):
        if isinstance(name, str):
            self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        if isinstance(rollNumber, int):
            self.__rollNumber = rollNumber


student_details = Student()

name = input("Enter the student's name: ")
rollNumber = int(input("Enter the student's roll number: "))

student_details.setName(name)
student_details.setRollNumber(rollNumber)


print("Name:", student_details.getName())
print("Roll Number:", student_details.getRollNumber())
