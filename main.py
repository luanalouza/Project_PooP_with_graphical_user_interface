import tkinter as tk
from gui import CarInputForm
from object_car import car
import pandas as pd
from pandas import *
import openpyxl
# Create a class to manage car data.
class CarManager:
    def __init__(self):
        # Initialize an empty list to store car objects.
        self.cars = []

    def add_car(self, brand, model, color, year, is_driving):
        # Create a new car and add it to the list.
        vehicle = car(brand, model, color, year, is_driving)
        self.cars.append(vehicle)

    def display_cars(self):
        # Display car info like brand, model, and more.
        for car in self.cars:
            print('Brand:', car.brand)
            print('Model:', car.model)
            print('Color:', car.color)
            print('Year:', car.year)
            if car.is_driving:
                car.drive()
            else:
                car.stop()

    def save_to_excel(self):
        # Prepare car data for export to Excel.
        car_data = []
        for car in self.cars:
            data = {
                'Brand': car.brand,
                'Model': car.model,
                'Color': car.color,
                'Year': int(car.year),
                'is_driving?': car.is_driving
            }
            car_data.append(data)

        # Print the car data for debugging.
        print("Debug - car_data:", car_data)

        # Save the car data to an Excel file.
        df = DataFrame(car_data)
        try:
            # Check if the Excel file exists and update it.
            existing_data = pd.read_excel('cars.xlsx')
            updated_data = pd.concat([existing_data, df], ignore_index=True)
            updated_data.to_excel('cars.xlsx', index=False)
        except FileNotFoundError:
            # If the file doesn't exist, create a new one.
            df.to_excel('./output_files/cars.xlsx', index=False)

if __name__ == '__main__':
    # Create a car manager instance.
    car_manager = CarManager()
    
    # Set up a GUI window for car input and interaction.
    root = tk.Tk()
    root.geometry("400x210")  
    form = CarInputForm(root, car_manager)
    root.mainloop()