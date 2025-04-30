#Activity 3: Deadline 2 May -  rewrite below sample code (from activity w3-6) 
#without using initializer & self (if it is possible?)

class Factorial:

    def factorial(number):  
        
        # Factorial check
        result = 1  
        for i in range(1, number + 1):
            result *= i
        return result
    
    # Prime check
    def Prime(number):
        # 0, 1 is not prime number
        if number < 2:  
            return False

        else:
            for i in range(2, int(number ** 0.5) + 1): 
                if number % i == 0:
                    return False
            return True
    
    def displayResult(number):
        print("Factorial of", number, "is", Factorial.factorial(number))

        if Factorial.factorial(number) == False:
            print(f"{number} is not a prime number.")
        else:
            print(f"{number} is a prime number.")

Factorial.displayResult(67)

 