# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox

#stores coffee types and their prices
COFFEE_PRICES = {
    "Latte": 5.50,
    "Cappuccino": 4.75,
    "Americano": 3.50
}
#function does validation, calculation, and displays results when calculate button is clicked
def calculate_spending():
    #gets user coffee type
    coffee_type = selected_coffee.get()
    
    #gets price for the selected coffee
    coffee_price = COFFEE_PRICES[coffee_type]
    
    #gets cups per day from user input
    cups_per_day_str = entry_cups.get()
    
    #validation that cups per day is a number
    try:
        cups_per_day = float(cups_per_day_str)
        
        #checks that number is positive
        if cups_per_day <= 0:
            #shows error popup if not
            messagebox.showerror("Invalid Input", "Please enter a positive number for cups per day!")
            return
            
    except ValueError:
        #shows error popup if not a valid number
        messagebox.showerror("Invalid Input", "Please enter a valid number for cups per day!")
        return
    
    #calculates daily cost of coffee 
    daily_cost = coffee_price * cups_per_day
    
    #performs calculations for different time periods
    weekly = daily_cost * 7
    monthly = daily_cost * 30
    yearly = daily_cost * 365
    
    #string manipulation: formats the coffee type for display
    display_name = coffee_type.capitalize()
    
    #updates labels with calculated values
    label_result_title.config(text=f"Your {display_name} Spending:")
    label_price_info.config(text=f"(${coffee_price:.2f} x {cups_per_day} cup(s) = ${daily_cost:.2f}/day)")
    label_weekly.config(text=f"Weekly: ${weekly:.2f}")
    label_monthly.config(text=f"Monthly: ${monthly:.2f}")
    label_yearly.config(text=f"Yearly: ${yearly:.2f}")
    label_message.config(text=f"That's a lot of {display_name.lower()}! ☕")
    
    #shows the results
    frame_results.pack(pady=20)


#creates main window
root = tk.Tk()
root.title("Coffee Budget Calculator")
root.geometry("400x670")
root.configure(bg="#FFF8DC")

#header of window
label_header = tk.Label(
    root, 
    text="☕ Coffee Budget Calculator", 
    font=("Arial", 18, "bold"),
    bg="#FFF8DC",
    fg="#8B4513"
)
label_header.pack(pady=20)

label_subtitle = tk.Label(
    root,
    text="Find out how much you spend on your daily coffee habit!",
    font=("Arial", 10),
    bg="#FFF8DC",
    fg="#666666"
)
label_subtitle.pack(pady=5)

#input frame
frame_input = tk.Frame(root, bg="#FFF8DC")
frame_input.pack(pady=20, padx=30)

#coffee type selection with buttons
label_coffee_type = tk.Label(
    frame_input,
    text="Select your coffee type:",
    font=("Arial", 10, "bold"),
    bg="#FFF8DC"
)
label_coffee_type.grid(row=0, column=0, sticky="w", pady=5)

#variable to store user coffee type
selected_coffee = tk.StringVar(value="Latte")

#buttons for each coffee option with prices displayed
radio_latte = tk.Radiobutton(
    frame_input,
    text="Latte - $5.50",
    variable=selected_coffee,
    value="Latte",
    font=("Arial", 10),
    bg="#FFF8DC"
)
radio_latte.grid(row=1, column=0, sticky="w", pady=2)

radio_cappuccino = tk.Radiobutton(
    frame_input,
    text="Cappuccino - $4.75",
    variable=selected_coffee,
    value="Cappuccino",
    font=("Arial", 10),
    bg="#FFF8DC"
)
radio_cappuccino.grid(row=2, column=0, sticky="w", pady=2)

radio_americano = tk.Radiobutton(
    frame_input,
    text="Americano - $3.50",
    variable=selected_coffee,
    value="Americano",
    font=("Arial", 10),
    bg="#FFF8DC"
)
radio_americano.grid(row=3, column=0, sticky="w", pady=2)

#cups per day input
label_cups = tk.Label(
    frame_input,
    text="How many cups per day? *",
    font=("Arial", 10, "bold"),
    bg="#FFF8DC"
)
label_cups.grid(row=4, column=0, sticky="w", pady=(15, 5))

entry_cups = tk.Entry(frame_input, width=30, font=("Arial", 11))
entry_cups.grid(row=5, column=0, pady=5)

#calculate button
button_calculate = tk.Button(
    root,
    text="Calculate My Coffee Spending",
    command=calculate_spending,
    font=("Arial", 12, "bold"),
    bg="#D2691E",
    fg="white",
    padx=20,
    pady=10,
    cursor="hand2"
)
button_calculate.pack(pady=20)

#results frame
frame_results = tk.Frame(root, bg="#FFE4B5", relief="solid", borderwidth=2)

label_result_title = tk.Label(
    frame_results,
    text="",
    font=("Arial", 14, "bold"),
    bg="#FFE4B5",
    fg="#8B4513"
)
label_result_title.pack(pady=10)

label_price_info = tk.Label(
    frame_results,
    text="",
    font=("Arial", 9),
    bg="#FFE4B5",
    fg="#666666"
)
label_price_info.pack(pady=2)

label_weekly = tk.Label(
    frame_results,
    text="",
    font=("Arial", 11),
    bg="#FFE4B5"
)
label_weekly.pack(pady=3)

label_monthly = tk.Label(
    frame_results,
    text="",
    font=("Arial", 11),
    bg="#FFE4B5"
)
label_monthly.pack(pady=3)

label_yearly = tk.Label(
    frame_results,
    text="",
    font=("Arial", 11, "bold"),
    bg="#FFE4B5",
    fg="#D2691E"
)
label_yearly.pack(pady=3)

label_message = tk.Label(
    frame_results,
    text="",
    font=("Arial", 9, "italic"),
    bg="#FFE4B5",
    fg="#666666"
)
label_message.pack(pady=10)

#runs the application
root.mainloop()