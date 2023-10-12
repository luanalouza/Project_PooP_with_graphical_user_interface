

class car:
    # Constructor to initialize car attributes: brand, model, color, year, and its driving state.
    def __init__(self, brand, model, color, year, is_driving):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.is_driving = is_driving

    # Method to simulate the car's motion.
    def drive(self):
        print(f"{self.brand} {self.model} is now in motion.")

    # Method to simulate the car coming to a stop.
    def stop(self):
         print(f"{self.brand} {self.model} has safely stopped.")

if __name__ == "__main__":
    # Create an instance of the 'car' class with sample details.
    my_car = car("Sample Brand", "Sample Model", "Red", 2022, True)
    
    # Demonstrate the car's actions: driving and stopping, and provide informative messages.
    my_car.drive()
    my_car.stop()
