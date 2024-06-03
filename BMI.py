import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        bmi = weight / (height / 100) ** 2
        bmi = round(bmi, 2)
        result_label.config(text=f"BMI: {bmi}")

        # Display BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        category_label.config(text=f"Category: {category}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for height and weight.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place the height label and entry
tk.Label(root, text="Height (cm):").grid(row=0, column=0, padx=10, pady=10)
entry_height = tk.Entry(root)
entry_height.grid(row=0, column=1, padx=10, pady=10)

# Create and place the weight label and entry
tk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=10)
entry_weight = tk.Entry(root)
entry_weight.grid(row=1, column=1, padx=10, pady=10)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create and place the result labels
result_label = tk.Label(root, text="BMI: ")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

category_label = tk.Label(root, text="Category: ")
category_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()