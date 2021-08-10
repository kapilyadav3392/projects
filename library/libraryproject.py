
class Library:

    def __init__(self, ListOfBooks):
        self.books = ListOfBooks

    def DisplayBooks(self):
        print('Available Books in library')
        for book in self.books:
            print(' *' + book)

    def BorrowedBook(self, bookName):
        if bookName in self.books:
            print(f"Book {bookName} issued you, keep it safe")
            self.books.remove(bookName)
            return True
        else:
            print('SORRY! this book is not available now or already issued to someone ')
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book.")


class Student:

    def __init__(self, Namelist):
        self.name = Namelist

    def displaystudents(self):
        for name in self.name:
          
            print(f"*" + name)

    def requestBook(self):
        self.book = input('Enter the name of the book you want : ')

        return self.book

    def returnBook(self):
        self.book = input('Book name you want to return: ')

        return self.book


if __name__ == "__main__":
    Name = Student(['pushpend', 'kapil'])

    Mylibrary = Library(["life", "friend", "way", "doIt", "sucess"])

    wlcmsg = ''' **********WELCOME TO MY LIBRARY**********
                    
                    -----list of students-----'''
    List = '''     
                    1. List of available books
                    2. Request for book
                    3. Return or Donate book
                    4. Exit the library'''
    
    print(wlcmsg)

    while(True):
       

        Name.displaystudents()

        b = input('student = ')
        if b == 'pushpend':
            while(True):
                print(List)

                a = int(input('Enter a choice: '))

                if a == 1:
                    Mylibrary.DisplayBooks()

                elif a == 2:
                    Mylibrary.BorrowedBook(Name.requestBook())

                elif a == 3:
                    Mylibrary.returnBook(Name.returnBook())

                elif a == 4:
                    print('Thanks for coming')
                    break

                else:
                    print('choice not available, please  choose given choices')

        elif b == 'kapil':
            while(True):
                print(List)

                a = int(input('Enter a choice: '))

                if a == 1:
                    Mylibrary.DisplayBooks()

                elif a == 2:
                    Mylibrary.BorrowedBook(Name.requestBook())

                elif a == 3:
                    Mylibrary.returnBook(Name.returnBook())

                elif a == 4:
                    print('Thanks for coming')
                    break

                else:
                    print('choice not available, please  choose given choices')

        else:
            print("no student found")
