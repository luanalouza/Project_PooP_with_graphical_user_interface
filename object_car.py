

class car:
    def __init__(self, brand, model, color, year, is_driving):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.is_driving = is_driving

    def drive(self):
        print(f"{self.brand} {self.model} is now driving.")

    def stop(self):
        print(f"{self.brand} {self.model} has stopped.")


if __name__ == "__main__":
    car = car("Sample Brand", "Sample Model", "Red", 2022, True)
    car.drive()
    car.stop()
