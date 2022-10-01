# Lecture 1

'''
Python Basics
- Python is an example of an interpreted language (unlike C/C++ and Java)
- Each line is interpreted one at a time
- Does have some flexibility, especially when simply running a program from top-to-bottom
    - But is also dangerous since it doesn’t check for type errors and may fail in the middle of execution
- Python interactive shell (IDLE) can execute lines of code by typing it in
- Stores state of variables that can be reused, BUT…
    - Once you exit the interactive shell, memory is cleared and your work is lost
    - So python programs are usually NOT written in the interactive shell and in separate .py files
'''

'''
Python Buit-in Atomic Types
- Python has some basic types of data that come straight out-of-the-box
- Examples are integers (int) and floats (decimals)
    - May affect the output type you’re getting, even if it’s numerically the same

Ex.
>>> 2/2
1.0 # float
>>> 2 + 2
4 # int
>>> 2 + 2.0
4.0 # float

- And there are certain functionality that may work with certain types, but not others

>>> x = 10.0
>>> int(x)
10
>>> float(x)
10.0
>>> x = "10.0" # string type
>>> type(x)
<class 'str'>
>>> x = float(x)
>>> type(x)
<class 'float'>
>>> x = int(x)
>>> type(x)
<class 'int'>
>>> x = "10.0"
>>> x = int(x)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    x = int(x)
ValueError: invalid literal for int() with base 10: '10.0'
>>> len(x)
4
>>> len(float(x))
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    len(float(x))
TypeError: object of type 'float' has no len()
'''

'''
Relational and Logical Operators
- Output of these operators result in a Boolean value
    - True , False
- Boolean values are important for control structures (while loops, if statements)
- Basically, allows you to fine-tune your program and define what / when instructions should be executed.

Ex.
>>> 5 == 5
True
>>> 5 != 5
False
>>> 5 < 5
False
>>> 5 <= 5
True
>>> 5 > 4
True
>>> 4 >= 5
False
>>> True or False
True
>>> not False or False
True
>>> False and True
False
'''
