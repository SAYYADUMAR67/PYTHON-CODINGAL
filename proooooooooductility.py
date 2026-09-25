import tkinter as tk
from tkinter import messagebox
 
def calculate_product():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        product = num1 * num2

        label_result.config(text=f"Product: {product}", fg="green")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
        label_result.config(text="Product: Error", fg="red")
 
root = tk.Tk()
root.title("Product Calculator")
root.geometry("300x250")
 
label_num1 = tk.Label(root, text="Enter First Number:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)
 
label_num2 = tk.Label(root, text="Enter Second Number:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)
 
button_multiply = tk.Button(root, text="Calculate Product", command=calculate_product)
button_multiply.pack(pady=15)
 
label_result = tk.Label(root, text="Product: ", font=("Arial", 12, "bold"))
label_result.pack(pady=10)
 
root.mainloop()
 