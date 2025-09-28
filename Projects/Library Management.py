# Library Management Sysyem

class Library:
    def __init__(self,):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The Library has{self.noBooks} books The books are :")
        for book in self.books:
            print(book)


l1 = Library()
l1.addBook("Bibek book1")
l1.addBook("Bibek book2")
l1.addBook("Bibek book3")
l1.showInfo()


