# Lecture 5

'''
Pytest
- Pytest is a framework that allows developers to write tests to check
  the correctness of their code
- Gradescope actually uses pytest to check the “correct” answer with students’ submissions
- We can write functions that start with test_, and the body of the function
  can contain assert statements (as seen in lab00)
- Pytest will run each of these functions are report which tests passed and which tests failed

Ex. TestFile
Write a function biggestInt(a,b,c,d) that takes 4 int values and returns the largest

def biggestInt(a, b, c, d):
#    biggest = 0
    if a >= b and a >= c and a >= d:
#      biggest = a  
       return a
    if b >= a and b >= c and b >= d:
#      biggest = b
        return b
    if c >= a and c >= b and c >= d:
#      biggest = c
        return c
    return d
#    else:
#        biggest = d
#    return biggest

Command to run pytest on testFile.py:
- Navigate to the folder containing lecture.py and testFile.py
- (On mac terminal): python3 -m pytest testFile.py
'''  

'''
Operator Overloading
- We can define our own behavior for common operators in our classes
    - What does it mean if two student objects are equal
      (we defined it to mean perm numbers are equal)?
    - Or what does it mean to add (+) two students together?
    - Python allows us to define the functionality for operators!
    
Defining __str__
- When printing our defined objects, we may get something unusual.

Ex:
from Student import Student

s1 = Student("Gaucho", 1234567)
s2 = Student("Jane", 5555555)
print(s1) <Student.Student object at 0x7fd5380d8e80>

- All objects can be printed, but Python wouldn’t know what to print for
  user-defined objects like Student
- So it just prints the memory address (the 0x...) of where the object exists in memory
- In order to provide our own meaning of what Python should display when printing an object
  like Student, we will need to define a special __str__ method in our Student class
- Python will now use the return value of the __str__ method when
  determining what to display in the print statement
    - Now the print(s1) statement outputs Student name: Gaucho, perm: 1234567

Overriding the '+' operator
- What would it mean to add (+) two students together?
- Maybe we can return a list collection … could be useful … maybe?
Ex. 
x = s1 + s2 # returns a list of s1 + s2
print(type(x)) # list type

for i in x:
	print(i)

# Output of for loop
# Student name: Gaucho, perm: 1234567
# Student name: Jane, perm: 5555555

Overloading the ‘<=’ and ‘>=’ operator
Ex.
print(s1 <= s2) # True
print(s1 >= s2) # False
print(s1 == s2) # False
print(s1 < s2) # ERROR, we didn’t define the __lt__ method
'''

'''
Inheritance
- Inheritance is a way of extending the functionality
  and properties of an existing class
    - and allows us to add new features
    - and allows us to replace existing features
Ex. Animal --> Cow
- Note that the Cow’s constructor (__init__) was inherited from the
  class Animal as well as the getAttributes() method
- Also note that we didn’t need to define the getSound() method
  since it was inherited from Animal
- But in this case, this inherited method getSound() may not be what we want.
- So we can redefine its functionality in the Cow class!

- We changed the getSound() method in the Cow class, so in this case our
  Cow class overrode the getSound() method of Animal
- So now, cow objects will use its own version of getSound(),
  not the version that was inherited from Animal, as seen below:
  
from Animal import Animal
from Cow import Cow

c = Cow("Cow", "Betsy", "Moo")
# c.setSound("Moo") # Sets a Cow sound to "Moo"
print(c.getSound()) # Moo!

#a = Animal("Unicorn", "Lala")
#print(a.getAttributes())
#print(a.getSound()) # I’m an Animal!!!

- Note: The constructed object type will dictate which method in which class is called.
    - It first looks at the constructed object type and checks if there is
      a method defined in that class. If so, it uses that
    - If the constructed object doesn’t have a method definition in its class,
      then it checks the parent(s) it inherited from, and so on …
    - If there is no matching method call, then an error happens
'''
