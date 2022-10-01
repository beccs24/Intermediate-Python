# Student.py

class Student:
    '''Student class type that contains student values'''

    def __init__(self, name = None, perm = None): # constructor
        self.name = name # can set to None as default
        self.perm = perm # can set to None as default

    # setter method
    def setName(self, name):
        self.name = name
        
    def setPerm(self, perm):
        self.perm = perm

    # getter method
    def getName(self):
        return self.name

    def printAttributes(self):
        print(f"Student name: {self.name}, perm: {self.perm}")
        # can also be written as
        # print("Student name: {}, perm: {}" \
        #       .format(self.name, self.perm))

    # Add the __eq__ method in Student.py
    # s1 == s2, self is the left operand (s1), rhs is the right operand (s2)
    def __eq__(self, rhs):
        return self.perm == rhs.perm

    def __str__(self):
        ''' returns a string representation of a student '''
        return f"Student name: {self.name}, perm: {self.perm}"

    def __add__(self, rhs):
        ''' Takes two students and returns a list containing these two students '''
        return [self, rhs]

    def __le__ (self, rhs):
        '''Take two students and return True if the student is <= the other
           based on the lexicographical order of the name'''
        return self.name.upper() <= rhs.name.upper()

    def __ge__(self, rhs):
	''' Takes two students and returns True if the
		student is greater than or equal to the other
		student based on the lexicographical order
		of the name '''
	return self.name.upper() >= rhs.name.upper()

    # > __gt__
    # < __lt__
            
'''
s = Student()
s = Student("Chris Gaucho", 1111111)
s = Student(perm = 1234567)
s.setName("Chris Gaucho")
s.setPerm(1111111)
s.printAttributes()

- When defining methods, the self parameter represents the current object
  we’re calling the method on
- In the example above, s is the variable storing the created Student object.
- When we define the methods, the first parameter is the instance of the object stored in s
- We can then use and manipulate the state of the object with these methods using the self parameter
'''


'''
Default Constructor
- We can provide either default values or set values of the object when
  constructing it through the parameter list
- In the example above, we can set an empty object without any initial attributes,
  which may cause an error when trying to use them
- The constructor above will set self.name and self.perm to the value None,
  which doesn’t require the set methods to set these fields in the object.

Overloading Constructors
- We can even go a step further and define the attributes by putting them
  in the parameters when we create the object

Initializing Default Values in the Constructor
- In this case, we can pass in parameters or not.
  If not, then None will automatically be assigned to the self.name and self.perm
- Or we can pick and choose what to set.
Ex. 
s = Student(perm=1234567)
s.printAttributes()

# Student name: None, perm: 1234567
- We used the default value of name (None) and then explicitly set the perm (1234567)
'''

'''
Example of Using Objects in Code

s1 = Student("Jane", 1234567)
s2 = Student("Joe", 7654321)
s3 = Student("Jill", 5555555)

studentList = [s1, s2, s3]

for s in studentList:
    s.printAttributes()

# Using assert statements to test correct functionality
s1 = Student()
assert s1.name == None
assert s1.perm == None


s1 = Student("Richert", 1234567)
s2 = Student("Gaucho", 7654321)
assert s1.name == "Richert"
assert s1.perm == 1234567
assert s2.name == "Gaucho"
assert s2.perm == 7654321
'''
