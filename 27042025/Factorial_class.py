# Function
#def catmeow():
#    print("Meow")


class Factorial:

    #initalize
    def __init__(self,num):
            self.num = num

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


'''
    def primeFactorial(self):
        
        prime = int(input("Enter the number you want to check prime number: "))
        
        if prime == 2 or prime == 3:
            print((f"{prime} is prime number"))

        elif (prime % 2) != 0 or (prime % 3) != 0:
            print(f"{prime} is prime number")

        else:
            print(f"{prime} is not prime number")
'''



number = int(input("What's the number? "))

# Create object
fact = Factorial(number)
fact.factorial()
fact.primeFactorial()


    