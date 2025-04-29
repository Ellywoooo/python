#Activity1 : Deadline 2 May - Library Book Manager Using classes
#Task: Manage a small library — add and show books.
 
class Books:

    #Constructor
    def __init__(self):
        print("******************************")
        print("***** Welcom to library! *****")
        print("******************************")
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

        print("\n----------- Book list -----------\n")
        for i in self.books:
            print(i)

    def options(self):
        
        while True:
            print("\n----------- Options -----------")
            print("\n\t(1) Add book")
            print("\t(2) Show book list")
            print("\t(3) Exit\n")
            print("-------------------------------")

            number = input("---- Choose the option! ----\n-->")

            if number == "1":
                self.add_Book()
            elif number == "2":
                self.show_Book()
            elif number =="3":
                print("Close the systme..")
                break
            else:
                print("Please choose the number 1-3 !")        
            

#Create object
newbook = Books()
newbook.options()