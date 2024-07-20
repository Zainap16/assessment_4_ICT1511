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
        
      
book1 = Book("1984", "George Orwell", "1234567890", "Dystopian")
book2 = Book("The Catcher in the Rye", "J.D. Salinger", "6677889900", "Classic", False)

# print(book1.title)
# print(book1.getTitle())

# print("This is where the chnage occurs")
# book1.setTitle("This is a new title")
# print(book1.title)
# print(book1.getTitle())

class Library:
    def __init__(self):
        self.books = []
        
    def addBook(self, book):
        self.books.append(book)
        return f"The book '{book.title}' has been added to library"
    
    def removeBook(self, ISBN):
        for book in self.books:
            if book.getISBN() == ISBN:
                self.books.remove(book)
                return f"the book 'book.title' has been removed from our library"
            return "Book not found"
    
    # def displayAvailableBooks(self):
    #     for book in self.books:
    #         if book.isAvailable() == False:
    #             return "No books currently is available"
    #         return f" Title: '{book.getTitle()}', Author: " #fill in entire sequence
    def display_available_books(self):
        available_books = [book for book in self.books if book.isAvailable()]
        if not available_books:
            return "No books are currently available."
        return "\n".join([f"Title: {book.getTitle()}, Author: {book.getAuthor()}, ISBN: {book.getISBN()}, Genre: {book.getGenre()}" for book in available_books])

    
    def searchByTitle(self, title):
        pass
        
        
                
        
library = Library()

library.addBook(book1.getAuthor())
library.addBook(book2.getAuthor())




