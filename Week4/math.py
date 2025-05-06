import math
# Last activity for Week 4: Using union and symmetric difference and Math and circle Libs
# Update the data format file to be added two more functionalities:
# 1- call Math function and get value from end user to calculate Sin and Cos
# 2- get diameter of a circle and calculate area of the circle.
# 3- Try to test the union and symmetric difference methods
 
class Circle:

    def __init__(self):
        
        self.degree = float(input("Enter your degree: "))
        self.diameter = float(input("Enter your diameter: "))

    def sincos_Math(self):    
        
        self.radions = math.radians(self.degree)
        print(f"sin: {math.sin(self.radions)} cos: {math.cos(self.radions)}")
    
    def area_circle(self):
        self.radius = self.diameter / 2
        self.area = math.pi * (self.radius ** 2)
        print(f"Area of circle : {self.area}")

class Diagram:

    def __init__(self):
        
        print("\n********************************")
        print("******* Ven Diagram Test *******")
        print("********************************\n")
        
        self.household_animals = {"cat","dog","parrot", "goldfish"}
        self.farmyards_animals = {"pig", "dog", "sheep", "cow", "horse"}
    
    def union_test(self):
        print(f"Union : {self.household_animals.union(self.farmyards_animals)}")
    
    def symmetric_test(self):
        print(f"Symmertric : {self.household_animals.symmetric_difference(self.farmyards_animals)}")
    
def main():
    circle = Circle()
    circle.sincos_Math()
    circle.area_circle()
    
    diagram = Diagram()
    diagram.union_test()
    diagram.symmetric_test()

if __name__ == "__main__":
    main()