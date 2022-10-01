# Lecture 11

from Lecture10 import *

def test_NodeCreation():
    n = Node(20)
    assert n.getData() == 20
    assert n.getNext() == None


def testNodeSetData():
    n = Node(20)
    n.setData(200)
    assert n.getData() == 200


def test_NodeSetNext():
    n = Node(20)
    n2 = Node(10)
    n.setNext(n2)
    assert n.getNext() == n2
    assert n.getNext().getData() == 10


def test_createList():
    ll = LinkedList()
    assert ll.isEmpty() == True


def test_addingNodesToList():
    ll = LinkedList()
    ll.addToFront(10)
    ll.addToFront("Gaucho")
    ll.addToFront(False)
    assert ll.isEmpty() == False
    assert ll.length() == 3
    assert ll.search(10) == True
    assert ll.search("Gaucho") == True
    assert ll.search(False) == True
    assert ll.search("CS9") == False    


def test_removeNodesFromList():
    ll = LinkedList()
    ll.addToFront(10)
    ll.addToFront("Gaucho")
    ll.addToFront(False)
    ll.addToFront("CS9")
    assert ll.length() == 4
    assert ll.search(10) == True
    ll.remove(10)
    assert ll.search(10) == False
    assert ll.search("Gaucho") == True
    assert ll.search(False) == True
    assert ll.search("CS9") == True
    assert ll.length() == 3
    ll.remove(False)
    assert ll.search(False) == False
    assert ll.search("Gaucho") == True
    assert ll.search("CS9") == True
    assert ll.length() == 2
    assert ll.isEmpty() == False
    ll.remove("Gaucho")
    ll.remove("CS9")
    ll.isEmpty() == True
    ll.length() == 0

def test_indexNode():
    ll = LinkedList()
    ll.addToFront(30)
    ll.addToFront(10)
    ll.addToFront(20)

    assert ll.index(30) == 2
    assert ll.index(20) == 0
    assert ll.index(10) == 1
'''
Ordered Linked List
- We've discussed Unordered Linked Lists where the position of the nodes
  did not matter with respect to each other
- Similar to an Unordered Linked List except (as you might guess)
  the nodes in the list are ordered with respect to each other
- The implementation of both are similar, except we have to maintain
  the ordered property of the nodes when we manage the list
    - Most methods can be the same, but adding the node requires us to put a node
      in the correct position (instead of simply adding to the front of the list)
    - Consider two cases:
        1. Adding to the front of the Linked List
        2. Adding to the middle / end of the Linked List

- Note that there are many variations on maintaining Linked Lists
    - Some variations improve the performance on certain methods
    - Ex.
        - Linked List with head AND tail references
        - Double-Linked List
        - Circular Linked List
        - etc.
    - Depending on what you need the data structure for,
      you can design variations to possibly improve your application
''' 


class OrderedLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def length(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.getNext() # taking a step down the list
        return count

    def search(self, item):
        temp = self.head
        found = False
        while temp != None and not found:
            if temp.getData() == item:
                found = True
            else:
                temp = temp.getNext()
        return found

    def remove(self, item):
        '''Removes first occurrence of item in the Linked List'''
        current = self.head
        if current == None: # empty list, nothing to do
            return

        previous = None
        found = False

        while not found: # Find the element
            if current == None:
                return
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # Case 1
        if found == True and previous == None:
            self.head = current.getNext()

        # Case 2
        if found == True and previous != None:
            previous.setNext(current.getNext())
                
    def add(self, item):
        current = self.head
        previous = None
        stop = False

        # find the correct place in the list to add a node
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        # Create node with the item to add
        temp = Node(item)

        # Case 1: insert at the front of the list
        if previous == None:
            temp.setNext(self.head)
            self.head = temp

        # Case 2:
        else:
            temp.setNext(current)
            previous.setNext(temp)

    # Method to get items from front to back
    # used for testing
    def getList(self):
        current = self.head
        output = ''
        while current != None:
            output += str(current.getData()) + ' '
            current = current.getNext()
        output = output[:len(output) - 1] # remove end space
        return output


def test_insertIntoOrderedList():
    ll = OrderedLinkedList()
    ll.add(35)
    ll.add(50)
    ll.add(10)
    ll.add(40)
    ll.add(20)
    ll.add(30)
    assert ll.getList() == "10 20 30 35 40 50"
    ll.add(5)
    assert ll.getList() == "5 10 20 30 35 40 50"
    ll.add(60)
    assert ll.getList() == "5 10 20 30 35 40 50 60"

            
'''
Quadratic Sorting Algorithms
- So far, we've discussed sorting through a list
    - Linear search - start at the beginning and check every element in the list
        - Does not require elements to be sorted
        - O(n) complexity
    - Binary search - check the middle, then check left or right sub lists
        - Does require elements to be sorted
        - O(log n) complexity
- But we haven’t discussed HOW to sort an unordered list
- There are many ways to do this, and some approaches are better than others.
  We’ll discuss several sorting algorithms and analyze their performance
- Quadratic Sorting Algorithms are done in O(n2)
'''

'''
Bubble Sort
- Idea: it will make several passes through the list and swap adjacent elements
        to ensure the largest element ends up at the end of the list (assuming we're
        sorting in ascending order)
'''

def bubbleSort(aList):
    for passnum in range(len(aList)-1, 0, -1):
        for i in range(passnum):
            if aList[i] > aList[i+1]:
                # swap (bubble up!)
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp

# bubbleSort pytest
def test_bubbleSort():
    list1 = [1,2,3,4,5,6]
    list2 = [2,2,2,2,2,2]
    list3 = [6,7,5,3,1]
    list4 = []
    bubbleSort(list1)
    assert list1 == [1,2,3,4,5,6]
    bubbleSort(list2)
    assert list2 == [2,2,2,2,2,2]
    bubbleSort(list3)
    assert list3 == [1,3,5,6,7]
    bubbleSort(list4)
    assert list4 == []
    
'''
Bubble Sort Analysis
- Notice that we have to make at most n-1 comparisons
  during the first iteration through the list
    - Then n-2 comparisons during the 2nd iteration, etc.
- So if we count the number of comparisons in this algorithm, we have
    - 1 + 2 + 3 + … + (n-2) + (n-1)
- This summation can be simplified to n(n+1)/2
    - We can deduce that this algorithm is O(n2)
- Also note that in the BEST case scenario, the list is already sorted
    - Each iteration does nothing, but we still compare the values anyways,
      thus performing unnecessary work
    - In order to improve situations where the list becomes sorted
      during the swaps, we can check if a swap occurred during an iteration
        - If yes, continue algorithm
        - If no, then the list is sorted, so stop the algorithm!
        - An implementation of this optimization is shown in the textbook
'''
        
