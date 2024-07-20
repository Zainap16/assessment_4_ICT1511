class Book:
    # intianlising
    def __init__(self,title,author, ISBN, genre, available=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.available = available
    
    # get methods
    
    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author
    
    def getISBN(self):
        return self.ISBN
        
    def getGenre(self):
        return self.genre
    
    def isAvailable(self):
        return self.available    
    
    # set methods - change values
    def setTitle(self, title):
        self.title = title 
    
    def setAuthor(self, author):
        self.author = author
    
    def setISBN(self, ISBN):
        self.ISBN = ISBN
        
    def setGenre(self, genre):
        self.genre = genre
    
    def setAvailability(self, available):
        self.available = available  

# Library class
class Library:
    def __init__(self):
        self.books = []
        
    def addBook(self, book):
        self.books.append(book)
        return f"The book '{book.getTitle()}' has been added to library"
    
    def removeBook(self, ISBN):
        for book in self.books:
            if book.getISBN() == ISBN:
                self.books.remove(book)
                return f"the book '{book.title}' has been removed from our library"
        return "Book not found"
    
    
    def displayAvailableBooks(self):
        available_books = []
        for book in self.books:
            if book.isAvailable():
                available_books.append(book)
        
        if not available_books:
            return "No books are currently available."
        
        book_details = []
        for book in available_books:
            details = (
                f"Title: {book.getTitle()}, "
                f"Author: {book.getAuthor()}, "
                f"ISBN: {book.getISBN()}, "
                f"Genre: {book.getGenre()}"
            )
            book_details.append(details)
        
        return "\n".join(book_details)

    
    def searchBookByTitle(self, title):
        foundBooks = []
        for book in self.books:
            if book.getTitle().lower() == title.lower():
                foundBooks.append(book)
        
        if not foundBooks:
            return "No book found!"
        
        result = []
        for book in foundBooks:
            result_book = f"Title: {book.getTitle()}, Author: {book.getAuthor()}, ISBN: {book.getISBN()}, Genre: {book.getGenre()}"
            result.append(result_book)
        
        return "\n".join(result)
    
    def searchBookByAuthor(self, author):
        foundBooks = []
        for book in self.books:
            if book.getAuthor().lower() == author.lower():
                foundBooks.append(book)
        
        if not foundBooks:
            return "No book found!"
        
        result = []
        for book in foundBooks:
            result_book = f"Title: {book.getTitle()}, Author: {book.getAuthor()}, ISBN: {book.getISBN()}, Genre: {book.getGenre()}"
            result.append(result_book)
        
        return "\n".join(result)
    
    def searchBookByGenre(self, genre):
        foundBooks = []
        for book in self.books:
            if book.getGenre().lower() == genre.lower():
                foundBooks.append(book)
        
        if not foundBooks:
            return "No book found!"
        
        result = []
        for book in foundBooks:
            result_book = f"Title: {book.getTitle()}, Author: {book.getAuthor()}, ISBN: {book.getISBN()}, Genre: {book.getGenre()}"
            result.append(result_book)
        
        return "\n".join(result)
    
    def addBookFromStaffMember(self, title, author, ISBN, genre, available = True):

        
        newBook = Book(title, author, ISBN, genre, available)
        self.addBook(newBook)
        
        return f"'{title}' by '{author}' (ISBN: '{ISBN}', Genre: '{genre}', Available: {available}) has been added to the library."
    
    def loanBook(self, ISBN):
        for book in self.books:
            if book.getISBN() == ISBN:
                if book.isAvailable():
                    book.setAvailability(False)
                    return f"'{book.getTitle()}' is now loaned out by you"
                else:
                    return f"'{book.getTitle()}' is currently unavailable"
                
        return "Book not found"
    
    def returnBook(self, ISBN):
        for book in self.books:
            if book.getISBN() == ISBN:
                if not book.isAvailable():
                    book.setAvailability(True)
                    return f"'{book.getTitle()}' is now returned back into library"
                else:
                    return f"'{book.getTitle()}' not loanded out/ is available"
        return "Book not found"
                
        

# dummy data

book1 = Book("1984", "George Orwell", "1234567890", "Dystopian",False)
book2 = Book("The Catcher in the Rye", "J.D. Salinger", "6677889900", "Classic")      
                
library = Library()

library.addBook(book1)
library.addBook(book2)

# print(library.returnBook("1234567890"))
# print(library.loanBook("6677889900"))
# print(library.displayAvailableBooks())
# print(library.searchBookByTitle("The Catcher in the Rye"))
# print(library.searchBookByAuthor("George Orwell"))
# print(library.searchBookByGenre("Classic"))

isTrue = True

while isTrue:
    print("Welcome staff member. Do you wish to add new books(add), remove books(remove), display avaible books(status), search books(search), process book loans(loan) and returns(return) /n Press q to quit")
    
    option = input("Which is your option: ")
        
    if option.lower() == "add":
        title = input("enter title: ")
        author = input("enter author: ")
        ISBN = input("enter ISBN: ")
        genre = input("enter genre: ")
        available = input("enter available: ")
        
        print(library.addBookFromStaffMember(title, author, ISBN, genre, available))
    
    
    if option.lower() == "remove":
        ISBN = input("enter ISBN: ")
        print(library.removeBook(ISBN))
        print(library.addBookFromStaffMember(title, author, ISBN, genre, str(available)))
        
    if option.lower() == "status":
        print(library.displayAvailableBooks())
        
    if option.lower() == "search":
        title = input("enter title of book: ")
        print(library.searchBookByTitle(title))
        
    if option.lower() == "loan":
        ISBN = input("enter ISBN: ")
        print(library.loanBook(ISBN))
        
    if option.lower() == "return":
        ISBN = input("enter ISBN: ")
        print(library.returnBook(ISBN))
    
    if option.lower() == "q":
        isTrue = False



