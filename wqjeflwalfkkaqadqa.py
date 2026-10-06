from tkinter import *
from tkinter import messagebox
 
# Function to perform the denomination calculation
def calculate_notes():
    try:
        amount = int(entry_amount.get())
        if amount < 0:
            messagebox.showerror("Error", "Please enter a positive amount.")
            return
 
        # Calculate number of notes for each denomination
        notes_2000 = amount // 2000
        amount %= 2000
 
        notes_500 = amount // 500
        amount %= 500
 
        notes_100 = amount // 100
        remainder = amount % 100
 
        # Update the result display labels
        lbl_res_2000.config(text=str(notes_2000))
        lbl_res_500.config(text=str(notes_500))
        lbl_res_100.config(text=str(notes_100))
 
        # Alert the user if there is a remainder that cannot be paid in these notes
        if remainder > 0:
            messagebox.showinfo("Notice", f"Remaining balance of {remainder} cannot be divided into 100, 500, or 2000 notes.")
 
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer amount.")
 
# Setting up Main Window
root = Tk()
root.title("Denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")
 
# Layout Configuration
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
 
# Heading
title_label = Label(root, text="Denomination Calculator", font=("Arial", 18, "bold"), bg="light blue")
title_label.grid(row=0, column=0, columnspan=2, pady=20)
 
# Input Section
lbl_amount = Label(root, text="Enter Amount:", font=("Arial", 12), bg="light blue")
lbl_amount.grid(row=1, column=0, sticky="e", padx=10, pady=10)
 
entry_amount = Entry(root, font=("Arial", 12), width=15)
entry_amount.grid(row=1, column=1, sticky="w", padx=10, pady=10)
 
# Calculate Button
btn_calculate = Button(root, text="Calculate", font=("Arial", 12, "bold"), command=calculate_notes, bg="white")
btn_calculate.grid(row=2, column=0, columnspan=2, pady=15)
 
# Results Section Header
lbl_heading_denom = Label(root, text="Denomination", font=("Arial", 12, "bold"), bg="light blue")
lbl_heading_denom.grid(row=3, column=0, pady=5)
 
lbl_heading_count = Label(root, text="Number of Notes", font=("Arial", 12, "bold"), bg="light blue")
lbl_heading_count.grid(row=3, column=1, pady=5)
 
# 2000 Notes Display
lbl_2000 = Label(root, text="Rs. 2000", font=("Arial", 11), bg="light blue")
lbl_2000.grid(row=4, column=0, pady=5)
lbl_res_2000 = Label(root, text="0", font=("Arial", 11, "bold"), bg="light blue")
lbl_res_2000.grid(row=4, column=1, pady=5)
 
# 500 Notes Display
lbl_500 = Label(root, text="Rs. 500", font=("Arial", 11), bg="light blue")
lbl_500.grid(row=5, column=0, pady=5)
lbl_res_500 = Label(root, text="0", font=("Arial", 11, "bold"), bg="light blue")
lbl_res_500.grid(row=5, column=1, pady=5)
 
# 100 Notes Display
lbl_100 = Label(root, text="Rs. 100", font=("Arial", 11), bg="light blue")
lbl_100.grid(row=6, column=0, pady=5)
lbl_res_100 = Label(root, text="0", font=("Arial", 11, "bold"), bg="light blue")
lbl_res_100.grid(row=6, column=1, pady=5)
 
# Start the application loop
root.mainloop()