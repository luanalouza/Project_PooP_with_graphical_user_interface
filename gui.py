import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CarInputForm:
    def __init__(self, root, car_manager):
        self.root = root
        self.root.title("Car Counter")
        self.car_manager = car_manager

        self.brand_options = ["Chrevrolet", "Tesla", "Fiat", "Wolkswagen", "Hyundai", "Mercedes", "Toyota"]
        self.color_options = ["Red", "Blue", "Green", "Black", "White","Yellow"]
        
    
       
        self.brand_label = ttk.Label(root, text="Brand:")
        self.brand_combo = ttk.Combobox(root, values=self.brand_options)
        self.model_label = ttk.Label(root, text="Model:")
        self.model_entry = ttk.Entry(root)  
        self.color_label = ttk.Label(root, text="Color:")
        self.color_combo = ttk.Combobox(root, values=self.color_options)
        self.year_label = ttk.Label(root, text="Year:")
        self.year_entry = ttk.Entry(root)
        self.is_driving_var = tk.BooleanVar()
        self.is_driving_checkbox = ttk.Checkbutton(root, text="Is Driving", variable=self.is_driving_var)
        self.save_button = ttk.Button(root, text="Save as Excel", command=self.save_data)
        self.submit_button = ttk.Button(root, text="Submit", command=self.submit)
        
        
        self.brand_label.grid(row=0, column=0)
        self.brand_combo.grid(row=0, column=1)
        self.model_label.grid(row=1, column=0)
        self.model_entry.grid(row=1, column=1)
        self.color_label.grid(row=2, column=0)
        self.color_combo.grid(row=2, column=1)
        self.year_label.grid(row=3, column=0)
        self.year_entry.grid(row=3, column=1)
        self.is_driving_checkbox.grid(row=4, columnspan=2)
        self.submit_button.grid(row=5, columnspan=2)
        self.save_button.grid(row=6, columnspan=2)
        
        car_image = Image.open("images\car_image.png")  
        car_image = car_image.resize((200, 200)) 
        self.car_photo = ImageTk.PhotoImage(car_image)
        self.car_image_label = ttk.Label(root, image=self.car_photo)
        self.car_image_label.grid(row=0, column=2, rowspan=7) 

    def submit(self):
        brand = self.brand_combo.get()
        model = self.model_entry.get() 
        color = self.color_combo.get()
        year = self.year_entry.get()
        is_driving = self.is_driving_var.get()
        
        
        if brand and model and color and year:
            self.car_manager.add_car(brand, model, color, year, is_driving)
        
   
        self.brand_combo.set("")
        self.model_entry.delete(0, tk.END)
        self.color_combo.set("")
        self.year_entry.delete(0, tk.END)

    def save_data(self):
        self.car_manager.save_to_excel()