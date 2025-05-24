# Is "car_name" variable is the same location in the memory? 
# Debug the code to get the name of the car from end user? See below code:

class RentalManager:
    _instance = None
    
    def user_input(self):
        self.car_name = input("Enter the car name: ")
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RentalManager, cls).__new__(cls)
            cls._instance.cars_available = ["Toyota", "Honda", "Ford"]
        return cls._instance
    def rent_car(self):
        if self.car_name in self.cars_available:
            self.cars_available.remove(self.car_name)
            print(f"{self.car_name} has been rented.")
        else:
            print(f"{self.car_name} is not available.")
 
    def show_available_cars(self):
        print("Available cars:", self.cars_available)
 
 
manager1 = RentalManager()
manager2 = RentalManager()


manager1.user_input() 
manager1.rent_car()
manager2.show_available_cars()  # Affects both because it's the same instance
 
print("Are both managers the same object?", manager1 is manager2)
print(f"manager1 id: {id(manager1)} and manager2 {id(manager2)}")