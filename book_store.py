class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        current_year = 2025
        return current_year - self.publication_year

    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"


book1 = Book("Gitanjali", "Rabindranath Tagore", "6465788797744", 1910)
book2 = Book("The Guide", "R.k Narayan", "656532689898", 1958)

print("Book 1 Title:", book1.title)
print("Book 1 Author:", book1.author)
print("Book 1 Age:", book1.get_age())
print("Book 1 Summary:", book1.get_summary())

print()

print("Book 2 Title:", book2.title)
print("Book 2 Author:", book2.author)
print("Book 2 Age:", book2.get_age())
print("Book 2 Summary:", book2.get_summary())
