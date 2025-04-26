class Factorial:
    
    def factorial(self):
   
        number = int(input("What's the number? "))
        fac = 1
        for i in range(1 , number+1):
            fac *= i
            print(f"{i}! is {fac}")


fact = Factorial()
fact.factorial()


    