# Creating Item (parent )class
class Item:
    def __init__(self, title, author, publication_year):
        self.author = author
        self.title = title
        self.publication_year = publication_year

    def display_details(self):
        print(f"Title of the item: {self.title}")
        print(f"Author of the item: {self.author}")
        print(f"Year the item was published: {self.publication_year}")

# Creating Book(child) class
class Book(Item):
    def __init__(self, title, author, publication_year, isbn):
        super().__init__(title, author, publication_year)
        self.isbn = isbn

    def display_details(self):
        super().display_details()
        print(f"ISBN: {self.isbn}")    

# Creating Journal(child) class
class Journal(Item):
    def __init__(self, title, author, publication_year, issn):
        super().__init__(title, author, publication_year)
        self.issn = issn

    def display_details(self):
        super().display_details()
        print(f"ISSN: {self.issn}")

# Creating library class and catalog
class Library:
    def __init__(self):
        self.catalog = []

    def add_item(self, item):
        self.catalog.append(item)

    def display_catalog(self):
        if not self.catalog:
            print ("Catalog is empty.")
        else:
            for i, item in enumerate(self.catalog, 1):
                print(f"\nItem {i}: ")
                item.display_details()

# Usage
library = Library()

book1 = Book("Archipelag GULag", "F. Soljenitsyn", 1981, "12124444")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "789456123")
journal1 = Journal("National Geographic", "Scientfic", 1990, "334455-01")

library.add_item(book1)
library.add_item(book2)
library.add_item(journal1)

library.display_catalog()
