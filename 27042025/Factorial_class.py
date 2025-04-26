# Function
#def catmeow():
#    print("Meow")


class Factorial:
    # Method
    def factorial(self):
   
        number = int(input("What's the number? "))
        fac = 1
        for i in range(1 , number+1):
            fac *= i
            print(f"{i}! is {fac}")

# Create object
fact = Factorial()
fact.factorial()


    