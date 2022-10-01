# Lecture 3

'''
Python Objects
- Objects are a way for programmers to define their own Python
  types and create abstractions of things with the programming language.
- Each object may have a certain state that gets modified throughout
  program execution
- Object Oriented (OO) programming is a way programs use and manipulate objects
  to solve problems and model real-world properties
- Object Oriented programming is NOT REQUIRED
    - It's more of a way to organize, read, maintain, test, and debut software
      in a manageable way

Ex. We've been using objects already...
>>> x = [1,2,3]
>>> type(x)
<class 'list'>
>>> x.count(3)
1
>>> x.count(-1)
0
>>> x.append(0)
>>> x
[1, 2, 3, 0]

- count, append, etc are all examples of methods that can be called on an object.
- Methods are like functions but are associated with an object
- In this case, Python already defined its own class called list that we can use,
  but sometimes we want to create our own specific objects for the applications
  we’re trying to build!

- Methods can be called on objects that have a state (values)
'''

'''
Refer to Student.py and Courses.py for example
'''
