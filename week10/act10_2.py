#Decompose the following function and share your results via a GitHub link. 
#See the function below:
 
import datetime

class Car:

    def database_car(self):
        self.cars = {
            "CAR001": {"type": "SUV", "available": True},
            "CAR002": {"type": "Sedan", "available": True},
            "CAR003": {"type": "Hatchback", "available": True}
        }
        self.users = ["user1", "user2"]
        self.rentals = {}
    
    def log_message(self, log_message):
        with open("rental_log.txt", "a") as log_file:
            log_file.write(log_message + "\n")
    
    def view_available_car(self):
        print("\nAvailable Cars:")
        for self.car_id, details in self.cars.items():
            if details["available"]:
                print(f"{self.car_id} - {details['type']}")
        log_message = f"{datetime.datetime.now()} - Viewed available cars"
        self.log_message(log_message)
    
    def rent_car(self):
        if self.car_id in self.cars and self.cars[self.car_id]["available"]:
            self.cars[self.car_id]["available"] = False
            self.rentals[self.user_id] = self.car_id
            print(f"{self.user_id} rented {self.car_id}")
            log_message = f"{datetime.datetime.now()} - {self.user_id} rented {self.car_id}"
            self.log_message(log_message)
        else:
            print("Car not available or invalid ID.")
            log_message = f"{datetime.datetime.now()} - {self.user_id} failed to rent {self.car_id}"
            self.log_message(log_message)

    def return_car(self, user_id):
        if user_id in self.rentals:
            self.car_id = self.rentals[user_id]
            self.cars[self.car_id]["available"] = True
            del self.rentals[self.user_id]
            print(f"{self.user_id} returned {self.car_id}")
            log_message = f"{datetime.datetime.now()} - {user_id} returned {self.car_id}"
            self.log_message(log_message)
        else:
            print("No rental record found.")
            log_message = f"{datetime.datetime.now()} - {user_id} attempted return with no rental"
            self.log_message(log_message)
    
    def car_rental_system(self):

        self.database_car()
    
        while True:
            print("\n--- Car Rental System ---")
            print("1. View Available Cars")
            print("2. Rent a Car")
            print("3. Return a Car")
            print("4. Exit")
            choice = input("Enter your choice: ")
    
            if choice == "1":
                self.view_available_car()
    
            elif choice == "2":
                self.user_id = input("Enter your user ID: ")
                if self.user_id not in self.users:
                    print("Invalid user.")
                    continue
                self.view_available_car()
                self.rent_car()
    
            elif choice == "3":
                self.user_id = input("Enter your user ID: ")
                self.return_car(self.user_id)
            
            elif choice == "4":
                print("Exiting system.")
                break
    
            else:
                print("Invalid choice.")
                log_message = f"{datetime.datetime.now()} - Invalid menu choice"
                self.log_message(log_message)

def main():
    rent = Car()
    rent.car_rental_system()

if __name__ == "__main__":
    main()