# Lecture 10

'''
Linked Lists
- Python lists are just one way to implement a List type structure
- The underlying structure of a Python List uses the concept of storing
  information in CONTIGUOUS memory
    - This is why certain operations like inserting into index 0 requires the shifting
      of elements to make room
- There is a another way to implement a List type structure that
  performs better in certain operations (and worse in others)
    - This way doesn't organize data in contiguous memory, so maintaining the
      list structure doesn't need to shift elements around
- LINKED LISTS is a list structure that is not stored in contiguous memory
    - BUT this structure still provides relative positioning of the
      data in the list

Node
- An item in the LinkedList
- Contains the data that we are storing in the list and a reference to the next Node
  in the Linked List

LinkedList
- Object that MANAGES and MAINTAINS the chain of nodes as a List collection
- Contains a head reference to the first node in the Linked List
    - As long as we know where the first element is, we can "walk" down
      the linked list and visit every node structure
- Methods in the LinkedList class should maintain the links between the nodes
    - These methods maintain the "links" between the nodes in order to keep the LinkedList
      structure in a valid state
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def addToFront(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp 
        

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
                
    def index(self, item):
        current = self.head
        previous = None
        count = 0
        
        while current != None:
            if current.getData() == item:
                return count
            else:
                previous = current
                current = current.getNext()
                count += 1

    def collectOdds(self):
        current = self.head
        oddList = []
        while current != None:
            if current.getData() % 2 != 0:
                oddList.insert(0, current.getData())
                current = current.getNext()
            else:
                current = current.getNext()
        return oddList


