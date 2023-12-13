class Book:
    def __init__(self,title, author,year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\n=========================")
   
to_kill_a_mockinbird = Book("To kill a mockinbird", "Harper Lee", 1960)
nineteen_eighty_four = Book("1984", "George Orwell", 1949)
to_kill_a_mockinbird.get_info()
nineteen_eighty_four.get_info()