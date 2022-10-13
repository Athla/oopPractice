#OOP IN PYTHON

class Student:
    #students attributes
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    #get grade method
    def getGrade(self):
        return self.grade
class Course:
    #course attributes
    def __init__(self, name, maxStudents):
        self.name = name
        self.maxStudents = maxStudents
        self.students = []
    #course methods
    def addStudent (self, student):
        if len(self.students) < self.maxStudents:
            self.students.append(student)
            return True
        return False
    def getAverage_Grade (self):
        value = 0
        for student in self.students:
            value += student.getGrade()
        return value / len(self.students)

s1 = Student("Athlas", 18, 90)
s2 = Student("Blake", 18, 95)
s3 = Student("Allya", 17, 100)

course = Course("Ap Math", 2)
course.addStudent(s1)
course.addStudent(s2)
print(course.addStudent(s3))
print(course.getAverage_Grade())