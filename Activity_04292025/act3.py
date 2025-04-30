#Activity 3: Deadline 2 May -  rewrite below sample code (from activity w3-6) 
#without using initializer & self (if it is possible?)

class Factorial:

    def factorial_Prime(number):  
        
        # Factorial check
        result = 1  
        #number = int(input("Enter the number you wat to check if it is Factorial and Prime: "))

        for i in range(1, number + 1):
            result *= i
        print("Factorial of", number, "is", result)
   
        # Prime check

        # 0, 1 is not prime number
        if number < 2:  
            print(f"{number} is not a prime number.")

        else:
            for i in range(2, int(number ** 0.5) + 1): 
                if number % i == 0:
                    print(f"{number} is not a prime number.")
                    break
                else:
                    print(f"{number} is a prime number.")
                    break

Factorial.factorial_Prime(66)

 