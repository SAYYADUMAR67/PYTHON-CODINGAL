import tkinter as tk
from tkinter import messagebox
 
def check_strength():
    password = password_entry.get()
    length = len(password)
    
    # Evaluate strength based on length
    if length == 0:
        result_label.config(text="Please enter a password.", fg="black")
    elif length < 6:
        result_label.config(text="Strength: Weak (Too short)", fg="red")
    elif 6 <= length <= 10:
        result_label.config(text="Strength: Medium", fg="orange")
    else:
        result_label.config(text="Strength: Strong", fg="green")
 
# Initialize the main Tkinter window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.config(bg="#f4f4f9")
 
# Application Heading
title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 16, "bold"), bg="#f4f4f9", fg="#333333")
title_label.pack(pady=15)
 
# Password Input Label
input_label = tk.Label(root, text="Enter your password:", font=("Arial", 11), bg="#f4f4f9")
input_label.pack(pady=5)
 
# Password Entry Widget (Masked input)
password_entry = tk.Entry(root, font=("Arial", 12), show="*", width=25)
password_entry.pack(pady=5)
 
# Check Button
check_button = tk.Button(root, text="Check Strength", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", command=check_strength, padx=10, pady=5)
check_button.pack(pady=15)
 
# Result Display Label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f4f4f9")
result_label.pack(pady=10)
 
# Run the Tkinter main event loop
root.mainloop()