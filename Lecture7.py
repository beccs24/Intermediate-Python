# Lecture 7

'''
Recursion
- When a function contains a call to itself
- Recursive solutions are useful when the result is dependent
  on the result of theh SUB-PARTS of the problem

The 3 laws of recursion
1. A recursive algorithm must have a BASE CASE
2. A recursive algorithm must change its state and move
   towards the base case
3. A recursive algorithm must call itself, recursively

Ex. Factorial
N! = N * (N-1) * (N-2) * ... * 2 * 1
N! = N * (N-1)!
0! = 1

def factorial(n): # n is a positive integer
    # base case
    if n == 0:
        return 1
    return n * factorial(n-1)

assert factorial(0) == 1
assert factorial(2) == 2
assert factorial(4) == 24
'''

'''
Function Calls and the Stack
- The Stack data structure has the First in, Last out (FILO) property
- We can only access the elements at the top of the stack
    - Analogy: Canister of tennis balls
        - In order to remove the bottom ball, we have to remove all the balls on top
- We won’t go through an implementation yet, but we can conceptualize this on a high-level
- Function calls utilize a stack (“call stack”) and organize how functions are called and how expressions that call functions wait for the functions’ return values
    - When a function is called, you can think of that function state being added (or “pushed”) on the stack
    - When a function finishes execution, it gets removed (or “popped”) from the stack
    - The top of the stack is the function that is currently running

Ex.
def double(n):
    return 2 * n

def triple(n):
    return double(n) + n

print(triple(5))


Ex. Fibonnacci
- A fibonacci sequence is the nth number in the sequence is the
  sum of the previous two (i.e. f(n) = f(n-1) + f(n-2)).
f(n) = f(n-1) + f(n-2)
f(0) = 0, f(1) = 1, f(2) = 1, f(3) = 2, f(4) = 3, f(5) = 5, f(6) = 8

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)
'''

'''
Python Lists vs. Python Dictionaries
- The following program counts the number of words in a file using a list and dictionary
    - They do the same thing, but the performance is vastly different…
    - wordlist.txt : File containing a collection of words, one per line.
    - PeterPan.txt : You can download classic novels from the Gutenberg Project as a .txt file!

# Set up data structures
DICT = {}
infile = open("wordlist.txt", 'r')
for x in infile: # x goes through each line in the file
    DICT[x.strip()] = 0
print(len(DICT))
infile.close()

WORDLIST = []
for y in DICT: # put the DICT keys into WORDLIST
    WORDLIST.append(y)
print(len(WORDLIST))

from time import time

# Algorithm 1 - Lists
start = time()
infile = open("PeterPan.txt", 'r')
largeText = infile.read()
infile.close()
counter = 0
words = largeText.split()
for x in words:
    x = x.strip("\"\'(){},.?!<>:;-").lower()
    if x in WORDLIST:
        counter += 1
end = time()
print(counter)
print("Time elapsed with WORDLIST (in sec):"), end - start


# Algorithm 2 - Dictionaries
start = time()
infile = open("PeterPan.txt", 'r')
largeText = infile.read()
infile.close()
counter = 0
words = largeText.split()
for x in words:
    x = x.strip("\"\'(){},.?!<>:;-").lower()
    if x in DICT:
        counter += 1
end = time()
print(counter)
print("Time elapsed with DICT (in sec):"), end - start

- Python lists are efficient if we know the index of the item we’re looking for
    - The reason why adding to the front of the list is costly is because
      lists have to “make room” for the element to be at index 0
        - All existing elements of the list need to shift one index up
          in order for the inserted element to be placed at index 0
    - Adding to the end of the list is not nearly as costly because
      no shifting of existing elements needs to occur
- For this example, since we are looking for the value in the list
  (without knowing the index), we are checking through the entire
  WORDLIST for every word in PeterPan.txt

- Python dictionaries are efficient when looking up a key value
    - Dictionary values are actually stored in an underlying list
    - Keys are converted into a numerical value, which is passed into a hash function
        - The purpose of the hash function is to output the index for the
          underlying list based on the key value
        - We do not have to scan the underlying list structure since a key
          will always be placed into a specific location in the the underlying list
        - We won’t go into the implementation now, but we’ll revist this in more detail later
- There are MANY ways to solve a problem in programming, but understanding
  how certain tools work and making the best decisions is important!
  
