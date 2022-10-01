class Book:
    
    def __init__(self, title = '', author = '', year = None):
        self.title = title
        self.author = author
        self.year = year

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def getBookDetails(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'

    def __gt__(self, rhs):
        if self.author > rhs.author:
            return True
        elif self.author < rhs.author:
            return False
        else:
            if self.year > rhs.year:
                return True
            elif self.year < rhs.year:
                return False
            else:
                if self.title > rhs.title:
                    return True
                elif self.title <= rhs.title:
                    return False
book = Book('sup', 'k', 2020)
print(book)
