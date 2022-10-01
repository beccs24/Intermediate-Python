# Lecture 4

'''
Shallow vs. Deep Equality
- Python allows us to check for equality using the == operator for our objects
- So by default, Python uses the memory address (not values) to determine
  if two objects are the "same"
- This is known as SHALLOW EQUALITY

Ex.
from Student import Student

s1 = Student("Jane", 1234567)
s3 = s1
s2 = Student("Jane", 1234567)

print(s1 == s2) # False, doesn't compare values
print(s1)
print(s2)

- In order to provide our meaning of equality for two Student objects,
  we will have to define the __eq__ method in our Student class
- In this case, we can assume two Students are the same
  if they have the same perm number
- Comparing values (instead of memory addresses) is called DEEP EQUALITY

Ex.
from Student import Student

s1 = Student("Jane", 1234567)
s3 = s1
s2 = Student("Jane", 1234567)

print(s1 == s2) # True, compares the perm values!
print(s1)
print(s2)
'''

'''
Python Errors
- We’ve probably seen Python complain before even running the program

Ex. 
print("Start")
PYTHON!
print( Hello )

- In this case, the program didn’t run at all. Before anything happened
- Python basically is telling us that PYTHON! is a syntax error.
- Before any Python script runs, it gets parsed through and
  there’s a simple check to make sure all expressions are legal.
- If not, then it will state an error. Note that the program is not running at this time.
- If we remove the syntactically incorrect line:

Ex.
print("Start")
print( Hello )

- We get another type of error that happens WHILE the code is executing.
- Errors that happen during program execution is called a runtime error:

Traceback (most recent call last):
  File "/Users/richert/Desktop/UCSB/CS9/lecture.py", line 5, in <module>
    print( Hello )
NameError: name 'Hello' is not defined

- The above message is basically saying Hello is a variable that hasn’t been defined,
  but we’re trying to use it in a print statement.
- Syntactically, there is nothing wrong with the above lines of code
  (since Hello could be a valid variable name).
- In this case, when python tries to execute the statement print( Hello ),
  it throws an exception
'''

'''
Exceptions
- Exceptions are errors that occur DURING program execution
- So far, when we’ve encountered these runtime errors,
  we’ve just noticed that the program crashes
- However, there are ways to recover from runtime errors
  since we can handle exceptions in our code
- In the above code segment, it’s complaining about a certain
  type of error called NameError
- There are many types of exceptions types that can occur during runtime.

Ex.
print("Start")
print (1/0)

- gives us the exception:

Traceback (most recent call last):
  File "/Users/richert/Desktop/UCSB/CS9/lecture.py", line 5, in <module>
    print( 1/0 )
ZeroDivisionError: division by zero

- In this case, the type of exception that has been thrown is called a
  ZeroDivisionError because a number divided by 0 is undefined

Ex.
print("Start")
print (‘5’ + 5)

- give us the exception:

Traceback (most recent call last):
  File "/Users/richert/Desktop/UCSB/CS9/lecture.py", line 5, in <module>
    print( '5' + 5 )
TypeError: can only concatenate str (not "int") to str

- In this case, a TypeError occurred since ‘+’ cannot add str types.
'''

'''
Handling Exceptions
- The general rule of exception handling is:
    - If an exception was raised in a program and nobody "catches" the
      exception error, then the program will terminate
- BUT we can handle except with a general structure referred to as
  try / except

Ex.
while True:
    try:
        # input() prompts user for input
        x = int(input("Enter an int: "))
        break # breaks out of the current loop
    except Exception:
        print("Input was not an int")
    print("Let's try again...")
print(x)
print("Resuming execution")

- The flow of execution is:
    - Everything within a try block is executed normally.
    - If an exception occurs in the try block, execution halts and
      an exception message is passed to a corresponding except block.
    - The except block tries to catch a certain exception type
      (note that Exception catches all types of exceptions
      (NameError, TypeError, ZeroDivisionError, etc)).
    - If there is a matching type in the except statements,
      then the first-matching except block is executed.
    - Once done, program execution resumes past the except block(s).
    - If no exceptions were caught, then the program will terminate with an error message.
'''

'''
Catching Multiple Exceptions
- Let’s slightly modify our code so another type of exception (ZeroDivisionError)
  may happen (in addition to entering a non-int type):

Ex.
while True:
    try:
        # input() prompts user for input
        x = int(input("Enter an int: "))
        print(x/0)
        break # breaks out of the current loop
    except ZeroDivisionError:
        print("Can't divide by zero")
    except Exception:
        print("Input was not an int")
    print("Let's try again...")

- In this case, the program will either complain that a number type was not entered,
  or if it was entered correctly, we’ll get a ZeroDivisionError
    - The program in this case will never execute “correctly”
- But the important thing to observe in this scenario is
  we can catch multiple exception types - depends on what type of exception was thrown
- The rule is:
    - except statements are checked top-down
    - The first matching exception type block is then executed
    - Then the program jumps past ALL the except statements
      (only one except block is executed) and code execution resumes


Ex. functions raising exceptions that are caught by the caller
def divide(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError
    return numerator / denominator

try:
    print(divide(1,1))
    print(divide(1,0))
    print(divide(2,2)) # Notice this doesn't get executed
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

print("Resuming Execution...")

- In this scenario, we have an exception raised in the divide function
- Since there isn’t an except statement in divide(),
  the exception message gets passed to the calling function
    - Since divide was called in a try block,
      then we check the except statements for the first match
    - If a match exists, then the first except block is executed,
      then all except blocks are skipped and execution resumes
- If an exception is raised and we NEVER handle it in an except block,
  then Program will eventually crash with an error message (like we’ve seen)
'''

'''
TESTING
Complete Test: Testing every possible path through the code in every possible situation
    - Generally infeasible…
    - Imagine a simple program that takes in 4 integers and prints out the max
        - In Python3, the range of valid integers is a lot!
        - Limited to memory (unlike other languages like C++ / Java
          where an int type is stored in 32 bits (4 bytes)
        - The number of computations to test EVERY POSSIBLE combination
          of the 4 integers will take A LONG TIME to compute!
    - Unit Testing: Testing individual pieces (units) of a program to ensure correct behavior

Test Driven Development (TDD)
1. Write test cases that describe what the intended behavior of
   a unit software should be. Kinda like the requirements of your piece of software
2. Implement the details of the functionality with the intention of passing the tests
3. Repeat until tests pass.

- Imagine large software products where dozens of engineers are trying to
  add new features / implement optimizations all at the same time
- Having a “suite” of tests before deploying software to the public is essential
    - Someone may modify changes that work for a current version,
      but breaks functionality in a future version
    - Rigorous tests enable confidence in the stability in software
'''
