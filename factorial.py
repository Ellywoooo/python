def factorial(x, fac):
    for i in range(1 , x+1):
        fac *= i
        print(f"{i} factorial is {fac}")

x = int(input("What's the number? "))
fac = 1

factorial(x, fac)




    