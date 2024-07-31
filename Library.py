class Library:

    def __init__(self, book_name):
        self.book_name = book_name

class Book(Library):

    def __init__(self, title, author, isbn, dds, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.dds = dds
        self.genre = genre
        
class CD(Library):

    def __init__(self, title, author, upc):
        self.name = title
        self.author = author
        self.upc = upc

class DVD(Library):

    def __init__(self, name, upc):
        self.name = name
        self.upc = upc

class Magazine(Library):

    def __init__(self, title, upc, issue_number, volume):
        self.title = title
        self.volume = volume
        self.issue_number = issue_number
        self.upc=upc

class Contributor(Library):

    def __init__(self, name, books):
        self.name = name
        self.books = books                 # List of Book class objects 

class BookCatalog(Library):

    def __init__(self, books_list):
        self.books_list = books_list       # List of Book class objects 

    def title_search(self,book_title):
        for book in self.books_list:
            if book.title == book_title:
                print("Here are the details of the book:")
                print("Book title: ",book.title)
                print("Book author: ",book.author)
                print("Book available on shelf number: ",book.dds)
                print("Book genre: ",book.genre)
                break
        else:
            print("Sorry, book is not available in library!")
        
    def author_search(self,author_name):
        books=[]
        for book in self.books_list:
            if book.author == author_name:
                books.append(book)
        if len(books) == 0:
            print("Sorry, books of entered author are not available in library")
        else:
            for book in books:
                print(book.isbn, book.title, book.genre)
    
    def genre_search(self):
        genres_available= list(set([book.genre for book in self.books_list]))
        print("Available genres are:")
        print(genres_available)
        print()
        books=[]
        genre=input("Enter the genre of books to be searched: ")
        for book in self.books_list:
            if (book.genre).lower() == genre.lower():
                books.append(book)
        if len(books) == 0:
            print("Sorry, no books available in entered genre")
        else:
            for book in books:
                print(book.isbn,"-",book.title,"-",book.author)

book1=Book("The India Story","Bimal Jalal","12345","02","NonFiction")
book2=Book("Harry Potter","J.K. Rowling","23456","01","Fiction")
book3=Book("The Hunger Games","Suzanne Collins","34567","01","Fiction")
book4=Book("Mahabharata","Vyasa","45678","02","NonFiction")
book5=Book("Goosebumps","R.L. Stine","56789","01","Fiction")
cd1=CD("When God Whispers Your Name","Max Lucado","01")
magazine1=Magazine("Agni","78912","01","01")
magazine2=Magazine("New Yorker","89123","01","02")
magazine3=Magazine("Ploughshares","91234","02","01")
dvd1=DVD("Bhagavat Gita Study Guide with DVD","67891")
contributor1=Contributor("Vishal",[book1,book2])
catalog = BookCatalog([book1,book2,book3,book4,book5])
book1 = input("Enter the book to be searched: ") # Mahabharata
print()
catalog.title_search(book1)
print()
book2 = input("Enter the book to be searched: ") # Ponniyin Selvan
print()
catalog.title_search(book2)
print()
author1 = input("Enter the author's name of the book to be searched: ") # Harry Potter
print()
catalog.author_search(author1)
print()
author2 = input("Enter the author's name of the book to be searched: ") # Bimal Jalal
print()
catalog.author_search(author2)                                      
print()

# Asks the user for input : Fiction/ NonFiction
catalog.genre_search()
