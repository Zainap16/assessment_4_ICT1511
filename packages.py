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

print(book1.title)
print(book1.getTitle())

print("This is where the chnage occurs")
book1.setTitle("This is a new title")
print(book1.title)
print(book1.getTitle())