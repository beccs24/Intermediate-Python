from Book import *
from BookCollection import *
from BookCollectionNode import *

def testBook():
    # test __init__, getTitle, getAuthor, getYear, getBookDetails
    book1 = Book("Ready Player One", "Cline, Ernest", 2011)
    assert book1.getTitle() == "Ready Player One"
    assert book1.getAuthor() == "Cline, Ernest"
    assert book1.getYear() == 2011
    assert book1.getBookDetails() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011'

    book2 = Book()
    assert book2.getTitle() == ''
    assert book2.getAuthor() == ''
    assert book2.getYear() == None
    assert book2.getBookDetails() == 'Title: , Author: , Year: None'

    # test __gt__
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    assert (b2 > b3) == False
    assert (b1 > b2) == True
    assert (b0 > b1) == True
    assert (b1 > b0) == False
    assert (b3 > b1) == False
    assert (b1 > b3) == True 


def testBookCollection():
    # test __init__, isEmpty
    oll1 = BookCollection()
    assert oll1.isEmpty() == True

    # test getNumberOfBooks, insertBook, getBooksByAuthor
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)

    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.isEmpty() == False
    assert bc.getNumberOfBooks() == 4
    assert bc.getBooksByAuthor("KING, Stephen") == 'Title: Rage, Author: King, Stephen, Year: 1977\n\
Title: The Shining, Author: King, Stephen, Year: 1977\n\
Title: Cujo, Author: King, Stephen, Year: 1981\n'
    assert bc.getBooksByAuthor("Rowling, J.K.") == ''

    # test getAllBooksInCollection
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)

    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getNumberOfBooks() == 4
    assert bc.getAllBooksInCollection() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011\n\
Title: Rage, Author: King, Stephen, Year: 1977\n\
Title: The Shining, Author: King, Stephen, Year: 1977\n\
Title: Cujo, Author: King, Stephen, Year: 1981\n'

    # test removeAuthor
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)

    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    bc.removeAuthor("KING, Stephen")
    assert bc.getNumberOfBooks() == 1
    assert bc.getAllBooksInCollection() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011\n'
    bc.removeAuthor("CLINE, Ernest")
    assert bc.isEmpty() == True
    assert bc.getAllBooksInCollection() == ''
    
    # test recursiveSearchTitle
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    assert bc.recursiveSearchTitle("CUJO", bc.head) == True
    assert bc.recursiveSearchTitle("Twilight", bc.head) == False


def testBookCollectionNode():
    # test __init__, getData, getNext
    bc1 = BookCollectionNode(Book("The Shining", "King, Stephen", 1977))
    assert bc1.getData().getTitle() == "The Shining"
    assert bc1.getData().getAuthor() == "King, Stephen"
    assert bc1.getData().getYear() == 1977
    assert bc1.getData().getBookDetails() == 'Title: The Shining, Author: King, Stephen, Year: 1977'
    assert bc1.getNext() == None

    # test setData
    bc1.setData(Book("Cujo", "King, Stephen", 1981))
    assert bc1.getData().getTitle() == "Cujo"
    assert bc1.getData().getAuthor() == "King, Stephen"
    assert bc1.getData().getYear() == 1981
    assert bc1.getData().getBookDetails() == 'Title: Cujo, Author: King, Stephen, Year: 1981'

    # test setNext
    bc2 = BookCollectionNode(Book("Ready Player One", "Cline, Ernest", 2011))
    bc1.setNext(bc2)
    assert bc1.getNext() == bc2
    assert bc1.getNext().getData().getTitle() == "Ready Player One"
    assert bc1.getNext().getData().getAuthor() == "Cline, Ernest"
    assert bc1.getNext().getData().getYear() == 2011
    assert bc1.getNext().getData().getBookDetails() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011'
