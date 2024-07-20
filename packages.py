class Book:
    def __init__(self,title,author, ISBN, genre, status=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.status = status
        
        
        
book1 = Book("1984", "George Orwell", "1234567890", "Dystopian", True)
print(book1.author)