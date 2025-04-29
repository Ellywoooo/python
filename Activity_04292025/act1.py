#Activity1 : Deadline 2 May - Library Book Manager Using classes
#Task: Manage a small library — add and show books.
 
class Books:

    #Constructor
    def __init__(self):
        print("Welcom to library! ")
        self.books = []

    def add_Book(self):
        
        book = input("Please enter the book name: ")
        self.books.append(book)
        
        self.moreBook = input("Would you like to add another book? enter (y) or (n) ")
        
        if self.moreBook == "y":
            self.add_Book()
        elif self.moreBook == "n":
            print("------- Pressed no -------")
        else:
            print("Please enter either (y) or (n)")


    def show_Book(self):

        print("------- Showing the book list in library -------")
        for i in self.books:
            print(i)

#Create object
newbook = Books()
newbook.add_Book()
newbook.show_Book()