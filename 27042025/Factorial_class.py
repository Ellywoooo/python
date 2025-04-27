# Function
#def catmeow():
#    print("Meow")


class Factorial:

    #initalize
    def __init__(self):
        self.num = 0

    def InputNumber(self):
        
        self.num = int(input("What's the number? "))

        if self.num <= 0:
            print("Please input positive intergar")
            self.InputNumber()
        else:
            return True

    # Method
    def factorial(self):
   
        fac = 1
        for i in range(1 , self.num+1):
            fac *= i
        print(f"{i}! is {fac}")
        
    def primeFactorial(self):
        
        # if number is 2 or 3
        if 0 < self.num < 4:
            print((f"{self.num} is prime number"))

        elif (self.num % 2) == 0 or (self.num % 3) == 0:
            print(f"{self.num} is not prime number")

        else:
            print(f"{self.num} is prime number")



# Create object
fact = Factorial()
fact.InputNumber()
fact.factorial()
fact.primeFactorial()


    