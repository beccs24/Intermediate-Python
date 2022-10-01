from Book import *
from BookCollectionNode import *

class BookCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getNumberOfBooks(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.getNext() 
        return count

    def insertBook(self, book):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > book:
                stop = True
            else:
                previous = current
                current = current.getNext()


        temp = BookCollectionNode(book)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)


    def getBooksByAuthor(self, author):
        string = ''
        current = self.head
        previous = None

        while current != None:
            if current.getData().getAuthor().lower() == author.lower():
                string += current.getData().getBookDetails() + '\n'
                current = current.getNext()
            else:
                current = current.getNext()
        return string
    
    
    def getAllBooksInCollection(self):
        string = ''
        current = self.head
        previous = None

        while current != None:
            string += current.getData().getBookDetails() + '\n'
            current = current.getNext()
        return string

    
    def removeAuthor(self, author):
        current = self.head
        
        if current == None: 
            return

        previous = None
        
        found = False

        while not found: 
            if current.getData().author.lower() == author.lower():
                found = True
            else:
                previous = current
                current = current.getNext()
        
        while current != None and current.getData().author.lower() == author.lower():    
            current = current.getNext()

        if found == True and previous == None:
            self.head = current

        if found == True and previous != None:
            previous.setNext(current)

                
    def recursiveSearchTitle(self, title, bookNode):
        if bookNode == None:
            return False
        elif bookNode.getData().title.lower() == title.lower():
            return True
        else:
            return self.recursiveSearchTitle(title, bookNode.getNext())
