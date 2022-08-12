

class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("books present in this library are: ")
        for book in self.books:
            print("\t *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"you have been issued {bookName}. please keep it safe!! <3")
            self.books.remove(bookName)
            return True
        else:
            print("sorry,book is alreay issued to someone else or may not",end = "")
            print(  "available in the library...plzz wait untill avalability of the book :(")
                
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("thanks for returning this book...have a nice day:)")


class Student:
    def requestBook(self):
        self.book = input("enter the anme of book you want to borrow\n")
        return self.book

    def returnBook(self):
        self.book = input("enter the anme of book you want to return\n")
        return self.book


if __name__ == "__main__":
    LalluLibrary = Library(["algorithms", "django", "integer", "algebra"])
    Student = Student()
    # LalluLibrary.displayAvailableBooks()
    while (True):
        welcomeMsg = '''
        ****welcome to LalluLibrary****
                please choose an option
                    1. list of books
                    2. reqst a book
                    3. Add/return a book
                    4. exit the library'''

        print(welcomeMsg)
        a = int(input("enter a choice: "))
        if a == 1:
            LalluLibrary.displayAvailableBooks()
        elif a == 2:
            LalluLibrary.borrowBook(Student.requestBook())
        elif a == 3:
            LalluLibrary.returnBook(Student.returnBook())
        elif a == 4:
            print("thanks for choosing LalluLibrary :D")
            exit()
        else:
            print("invalid choice! -_-")
