class library:
    def __init__(self):
        self.books = []
        self.borrowed = []
    def add_books(self, title):
        self.books.append(title)
        print(f"{self.books} added successfully")
    def borrow_books(self, title):
        if title in self.books:
            self.books.remove(title)
            self.borrowed.append(title)
            print(f"you borrowed {title}")
        else:
            print(f"{title} not available")
    def return_books(self, title):
        if title in self.borrowed:
            self.borrowed.remove(title)
            self.books.append(title)
            print(f"you returned {title} successfully")
    def show_books(self):
           if not self.books:
               print("no books available")
           else:
               print("books in library")
               for book in self.books:
                   print("_", book)
lib = library()
lib.add_books("python 101")
lib.add_books("basics")
lib.show_books()
lib.borrow_books("python 101")
lib.show_books()
lib.return_books("python 101")
