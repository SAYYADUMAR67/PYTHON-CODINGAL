from datetime import date
import tkinter as tk
from tkinter import messagebox
 
 
def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
 
        birth_date = date(year, month, day)
        today = date.today()
 
        age = (
            today.year
            - birth_date.year
            - ((today.month, today.day) < (birth_date.month, birth_date.day))
        )
 
        result_label.config(
            text=f"Your Present Age is: {age} Years", fg="#1E8449"
        )
 
    except ValueError:
        messagebox.showerror(
            "Input Error", "Please enter valid integers for Day, Month, and Year."
        )
 
root = tk.Tk()
root.title("Age Calculator")
root.geometry("360x280")
root.config(padx=20, pady=20, bg="#F4F6F7")
root.resizable(False, False)
 
title_label = tk.Label(
    root, text="Age Calculator", font=("Arial", 16, "bold"), bg="#F4F6F7"
)
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
 
tk.Label(root, text="Day (DD):", font=("Arial", 10), bg="#F4F6F7").grid(
    row=1, column=0, sticky="w", pady=5
)
day_entry = tk.Entry(root, font=("Arial", 10), width=15)
day_entry.grid(row=1, column=1, pady=5)
 
tk.Label(root, text="Month (MM):", font=("Arial", 10), bg="#F4F6F7").grid(
    row=2, column=0, sticky="w", pady=5
)
month_entry = tk.Entry(root, font=("Arial", 10), width=15)
month_entry.grid(row=2, column=1, pady=5)
 
tk.Label(root, text="Year (YYYY):", font=("Arial", 10), bg="#F4F6F7").grid(
    row=3, column=0, sticky="w", pady=5
)
year_entry = tk.Entry(root, font=("Arial", 10), width=15)
year_entry.grid(row=3, column=1, pady=5)
 
calc_button = tk.Button(
    root,
    text="Calculate Age",
    font=("Arial", 11, "bold"),
    bg="#3498DB",
    fg="white",
    command=calculate_age,
    cursor="hand2",
)
calc_button.grid(row=4, column=0, columnspan=2, pady=20, sticky="we")
 
result_label = tk.Label(
    root,
    text="Enter your DOB details above.",
    font=("Arial", 12, "bold"),
    bg="#F4F6F7",
    fg="#7F8C8D",
)
result_label.grid(row=5, column=0, columnspan=2, pady=5)
 
root.mainloop()
 