# Lecture 6

'''
Extending Superclass Methods
- Some terminology:
- In the previous example, Animal can be referred to as the Base/Parent/Super class and
- Cow can be referred to as the Sub/Child/Derived class

- In the example, we overrode the makeSound method from Animal
- However, sometimes we only want to extend the functionality, not completely replace it.
- It is possible to override methods and still use the inherited functionality by
  calling the super() class methods
- So in this case, we override the method in the child class, but we extend the base class’ functionality by using it in the child class’ overwritten method

Ex. Cow
Output:
Using super class getSound method
I'm an Animal!!!
Extending it with our own getSound functionality
Moo!!!
'''

'''
Extending Constructors in a Child Class
- A common pattern is to redefine a subclass’ constructor by taking in
  all data from its parent class AND data specific to the subclass.

Ex. Cow
'''

'''
Inheritance and Exceptions
- We can create a hierarchy of Exception types using inheritance
    - Exception is the base class for ALL Exception types (Python allows us to raise these types)
    - Remember the sub-class IS-A type of the base class
    - This may be useful for fine-tuning certain behavior
    - For example, a network error could be because of:
        - Malformed URL
        - Timeout, etc...
- Or file reading may error out due to:
    - Incorrect file name
    - Incorrect access permissions, etc...

Ex. 
class A(Exception):
    pass

class B(A):
    pass

class C(Exception):
    pass


try:
    x = int(input("Enter a positive number: "))
    if x < 0:
        raise B()
except C:
    print("Exception of type C caught")
except A:
    print("Exception of type A caught")
except B:
    print("Exception of type B caught")
except Exception:
    print("Exception of type Exception caught")

print("Resuming execution")

- In the example above, B’s except block is never called.
    - This is because B IS-A type of A (B is a child of A).
      So when we catch the matching type, A always matches first.
'''

'''
Algorithm Analysis
- There are many ways we can try to estimate an algorithm
- For example, we can benchmark the algorithm by calculating the
  time it takes for something to run
- We can do this in Python using some code:

Ex.
import time

def f1(n):
    l = []
    for i in range(n):
        l.insert(0, i)
    return

def f2(n):
    l = []
    for i in range(n):
        l.append(i)
    return

print("starting f1")
start = time.time()
f1(200000)
end = time.time()
print("time elapsed: ", end - start, "seconds")

print("starting f2")
start = time.time()
f2(200000)
end = time.time()
print("time elapsed: ", end - start, "seconds")

- We’ll get to why the time difference between adding to the list
  in the beginning and adding to the end differ in time
- This way of measuring algorithms has some problems like:
    - Underlying hardware (fast / slow CPU, amount of memory, disk size / speed,
      network speed, etc.)
    - How busy the computer is, how the OS is managing other programs
    - How big n is (if n is small, time is almost the same)
'''

'''
Asymptotic Behavior
- We want to analyze approximately how fast an algorithm runs when the size
  of the input approaches infinity
- So instead of calculating the raw time of how fast the algorithm runs on
  our computers, we can approximate the number of instructions the algorithm
  will take with respect to the size of the input
    - Steps can include things like assigning values to variables, evaluating boolean expressions, arithmetic operations, etc.

Ex. 1)
for i in range(10):
    print(i)

- Counting expressions in this case:
    - Assignment: i = 0, i = 1, i = 2, etc. (10 steps)
    - print() (10 steps)
    - Algorithm takes 20 steps
- The algorithm runs in constant time, since there isn’t a variable input
  and will always take the same number of instructions to run.

Ex.2) 
def f(n):
    for i in range(n):
        print(i)

- Now the number of instructions in this algorithm is dependent on the value of n
- So let’s try to express the number of instructions as a polynomial with respect to n
    - We can denote the number of instructions with respect to n as T(n)
- T(n) = n assignment statements + n print statements
- T(n) = 2n
'''

'''
Order of Magnitude Function (Big-O)
- We can express the algorithm when the input approaches infinity
  by taking the time function (T(n)) and:
  - Drop all lower-order terms, coefficients, and constants to O(n)
  - Note: constant time algorithms are denoted as O(1)

Ex. 1)
def f(n):
    x = 0
    for i in range(n):
        for j in range(n):
            x = i + j

- Initialize x = 0 is 1 instruction
- i assignment statements (n instructions)
- j assignment statements (n2 instructions)
- i + j computations (n2 instructions)
- x reassignment statements (n2 instructions)
    - T(n) = 1 + 3n2 + n
- T(n) = 1 + n + n^2 + n^2 + n^2 = 3n^2 + n + 1
- O(n) = n^2


Common Big-O Notations
- From fastest to slowest
O(1): Constant
O(log n): Logarithmic
O(n): Linear
O(nlogn): Log Linear
O(n^2): Quadratic
O(n^3): Cubic
O(2^n): Exponential

Ex. 1)
def f(n):
    for i in range(0, n, 3):
        print(i)
- T(n) = n/3 + n/3 --> O(n)

Ex. 2)
def f(n):
    for i in range(n):
        return i
- T(n) = 1 + 1 = 2 --> O(1)
'''
