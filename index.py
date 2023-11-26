import tkinter as tk
from tkinter import messagebox

# Define the matrix of electricity consumption units
consumption_matrix = [
    [55, 65, 75],  # Slab 1 data
    [120, 150, 170],  # Slab 2 data
    [210, 230, 240]   # Slab 3 data
]

# Constants for unit costs per slab
COST_SLAB_1 = 10
COST_SLAB_2 = 15
COST_SLAB_3 = 20

# Function to calculate and display cost for slab 1
def costSlab1():
    costs = [unit * COST_SLAB_1 for unit in consumption_matrix[0]]
    messagebox.showinfo("Slab 1 Costs", f"Cost for Slab 1: {costs}")

# Function to calculate and display cost for slab 2
def costSlab2():
    costs = [unit * COST_SLAB_2 for unit in consumption_matrix[1]]
    messagebox.showinfo("Slab 2 Costs", f"Cost for Slab 2: {costs}")

# Function to calculate and display cost for slab 3
def costSlab3():
    costs = [unit * COST_SLAB_3 for unit in consumption_matrix[2]]
    messagebox.showinfo("Slab 3 Costs", f"Cost for Slab 3: {costs}")

# Create the main window
root = tk.Tk()
root.title("Electricity Bill Calculator")

# Label for the student ID
student_id_label = tk.Label(root, text="Student ID: 123")
student_id_label.pack()

# Buttons to display each slab's costs
button_slab1 = tk.Button(root, text="Display Bill of Slab 1 and Slab 2", command=lambda: [costSlab1(), costSlab2()])
button_slab1.pack(pady=5)

button_slab2 = tk.Button(root, text="Display Bill of Slab 3", command=costSlab3)
button_slab2.pack(pady=5)

# Run the application
root.mainloop()