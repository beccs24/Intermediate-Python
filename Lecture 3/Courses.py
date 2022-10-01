# Courses.py

# from [filename] import [component]
from Student import Student

class Courses:
    '''Class representing a collection of courses. Courses are organized
       by a dictionary where the key is the course number and the
       corresponding value is a list of Students in a course'''

    def __init__(self):
        self.courses = {}

    def addStudent(self, student, courseNum):
        '''Method adds a student object to a courseNum'''
        # If the course doesn't exist
        if self.courses.get(courseNum) == None:
            self.courses[courseNum] = [student]
        elif not student in self.courses.get(courseNum):
            self.courses[courseNum].append(student)
    
    def printCourses(self):
        for courseNum in self.courses:
            print("CourseNum: ", courseNum)
            for student in self.courses[courseNum]:
                student.printAttributes()
            print("---")

    # Getter method
    def getCourses(self):
        return self.courses

'''
Container Classes
- Let’s continue to expand on our Student class
- Classes are also useful to organize / maintain state of a program
- Student objects are useful to organize the attributes of a single student
- But let’s imagine we are trying to write a database of various students
    - The database may be useful to search for students with certain attributes…
    - We will need to add / remove things from our database
    - We can define a class to represent a collection of courses containing students
    - Let’s set up a collection of courses such that a dictionary key is defined
      by the course number and the value is a list of actual student objects
'''


# Using assert statements to test correct functionality
s1 = Student("Jane", 1234567)
s2 = Student("Joe", 7654321)
s3 = Student("Jill", 5555555)

UCSB = Courses()
UCSB.addStudent(s1, "CS8")
UCSB.addStudent(s2, "CS9")
UCSB.addStudent(s3, "CS16")
UCSB.addStudent(s2, "CS16")
courses = UCSB.getCourses()
UCSB.printCourses()

assert courses == {'CS8': [s1], 'CS9': [s2], 'CS16': [s3, s2]}
