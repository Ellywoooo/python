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
        
            for num in range(2, int(self.num**0.5)+ 1):
                
                if self.num % num == 0:
                    print(f"{self.num} is not prime number")
                else:
                    print(f"{self.num} is prime number")


# Create object
fact = Factorial()
fact.InputNumber()
fact.factorial()
fact.primeFactorial()


    