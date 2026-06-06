'''Books available in a library:
books = [
 ("Python Basics", 5),
 ("Data Science", 0),
 ("Java Programming", 3),
 ("Machine Learning", 0)
]
Write a program to:
• Display unavailable books.
• Find all books with more than 2 copies.
• Count available books.
• Stop searching once a requested book is found.'''
books = [
 ("Python Basics", 5),
 ("Data Science", 0),
 ("Java Programming", 3),
 ("Machine Learning", 0)
]
# Library Book Management System

# -----------------------------------
# Books data

books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# -----------------------------------
# Initialize variables

available_books_count = 0

print("Unavailable Books:")

# -----------------------------------
# Process book records

for book in books:

    book_name = book[0]
    copies = book[1]

    # Display unavailable books

    if(copies == 0):
        print(book_name)

    # Find books with more than 2 copies

    if(copies > 2):
        print("More Than 2 Copies:", book_name)

    # Count available books

    if(copies > 0):
        available_books_count = available_books_count + 1

# -----------------------------------
# Display available books count

print("\nAvailable Books Count:", available_books_count)

# -----------------------------------
# Search a requested book

requested_book = input("\nEnter Book Name to Search: ")

for book in books:

    if(book[0] == requested_book):

        print("Book Found:", book[0])
        break

else:

    print("Book Not Found")