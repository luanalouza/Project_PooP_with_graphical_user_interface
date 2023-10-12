import tkinter as tk
from gui import CarInputForm
from object_car import car
import pandas as pd
from pandas import *



class CarManager:
    def __init__(self):
        self.cars = []

    def add_car(self, brand, model, color, year, is_driving):
        vehicle = car(brand, model, color, year, is_driving)
        self.cars.append(vehicle)

    def display_cars(self):
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

        print("Debug - car_data:", car_data) 
        df = DataFrame(car_data)
        try:
            existing_data = pd.read_excel('cars.xlsx')
            updated_data = pd.concat([existing_data, df], ignore_index=True)
            updated_data.to_excel('cars.xlsx', index=False)
        except FileNotFoundError:
            df.to_excel('cars.xlsx', index=False)

if __name__ == '__main__':
    car_manager = CarManager()
    
    root = tk.Tk()
    root.geometry("400x210")  
    form = CarInputForm(root, car_manager)
    root.mainloop()
  
    car_manager.save_to_excel()
