import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
 
# This function does the math when you click the button
def calculate_interest():
    try:
        # 1. Get the numbers out of the boxes and turn them into decimal numbers (floats)
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())
        
        # Check if any numbers are negative
        if principal < 0 or rate < 0 or time < 0:
            messagebox.showerror("Oops!", "Numbers cannot be negative! Please enter positive numbers.")
            return
            
        # 2. THE MATH FORMULAS:
        # Simple Interest Formula: (Principal * Rate * Time) / 100
        simple_interest = (principal * rate * time) / 100
        total_simple_balance = principal + simple_interest
        
        # Compound Interest Formula: Principal * (1 + Rate/100)^Time - Principal
        # (Assuming it compounds once every year)
        total_compound_balance = principal * ((1 + (rate / 100)) ** time)
        compound_interest = total_compound_balance - principal
        
        # 3. SHOW THE RESULTS:
        # Update the labels to show the calculated amounts, rounded to 2 decimal places
        lbl_simple_res.config(text=f"Simple Interest Earned: ${simple_interest:,.2f}\n(Total Balance: ${total_simple_balance:,.2f})")
        lbl_compound_res.config(text=f"Compound Interest Earned: ${compound_interest:,.2f}\n(Total Balance: ${total_compound_balance:,.2f})")
        
        # Calculate the difference to see which one made more money
        difference = compound_interest - simple_interest
        lbl_diff_res.config(text=f"Compound interest made ${difference:,.2f} more than simple interest!")
        
        # 4. ADD TO THE HISTORY TABLE:
        # This lets you compare your different calculations!
        tree.insert('', 0, values=(
            f"${principal:,.2f}",
            f"{rate}%",
            f"{time} Years",
            f"${simple_interest:,.2f}",
            f"${compound_interest:,.2f}"
        ))
        
    except ValueError:
        # If someone types letters instead of numbers, show this friendly warning
        messagebox.showerror("Input Error", "Please only type normal numbers into the boxes!")
 
# This function clears all the text boxes to start fresh
def clear_all():
    entry_principal.delete(0, tk.END)
    entry_rate.delete(0, tk.END)
    entry_time.delete(0, tk.END)
    lbl_simple_res.config(text="Simple Interest Earned: $0.00")
    lbl_compound_res.config(text="Compound Interest Earned: $0.00")
    lbl_diff_res.config(text="")
 
# This clears out the history table
def clear_history():
    for item in tree.get_children():
        tree.delete(item)
 
# --- CREATING THE WINDOW LAYOUT ---
root = tk.Tk()
root.title("Fun & Easy School Interest Calculator 🧮")
root.geometry("750x550")
 
# Left Column for Inputs and Math Controls
left_frame = ttk.LabelFrame(root, text=" 1. Enter Your Math Data ", padding=10)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")
 
ttk.Label(left_frame, text="Starting Money (Principal $):").pack(anchor="w", pady=2)
entry_principal = ttk.Entry(left_frame, width=25)
entry_principal.pack(pady=2)
entry_principal.insert(0, "1000") # Default starting money
 
ttk.Label(left_frame, text="Interest Rate per Year (%):").pack(anchor="w", pady=2)
entry_rate = ttk.Entry(left_frame, width=25)
entry_rate.pack(pady=2)
entry_rate.insert(0, "5") # Default interest rate
 
ttk.Label(left_frame, text="Time Period (Years):").pack(anchor="w", pady=2)
entry_time = ttk.Entry(left_frame, width=25)
entry_time.pack(pady=2)
entry_time.insert(0, "3") # Default years
 
btn_calc = ttk.Button(left_frame, text="Calculate!", command=calculate_interest)
btn_calc.pack(fill="x", pady=10)
 
btn_clear = ttk.Button(left_frame, text="Clear Boxes", command=clear_all)
btn_clear.pack(fill="x", pady=2)
 
# Right Column for Math Results
right_frame = ttk.LabelFrame(root, text=" 2. See the Results ", padding=10)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
 
lbl_simple_res = ttk.Label(right_frame, text="Simple Interest Earned: $0.00")
lbl_simple_res.pack(anchor="w", pady=5)
 
lbl_compound_res = ttk.Label(right_frame, text="Compound Interest Earned: $0.00")
lbl_compound_res.pack(anchor="w", pady=5)
 
lbl_diff_res = ttk.Label(right_frame, text="", wraplength=350)
lbl_diff_res.pack(anchor="w", pady=10)
 
# Bottom Section for History / Comparing Numbers
bottom_frame = ttk.LabelFrame(root, text=" 3. Compare Your History Logs ", padding=10)
bottom_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
 
# Setup the history list columns
columns = ('principal', 'rate', 'time', 'simple', 'compound')
tree = ttk.Treeview(bottom_frame, columns=columns, show='headings', height=6)
tree.heading('principal', text='Starting Money')
tree.heading('rate', text='Rate')
tree.heading('time', text='Time')
tree.heading('simple', text='Simple Total')
tree.heading('compound', text='Compound Total')
 
# Set column widths
for col in columns:
    tree.column(col, width=130, anchor="center")
tree.pack(side="left", fill="both", expand=True)
 
btn_clear_hist = ttk.Button(bottom_frame, text="Clear History Table", command=clear_history)
btn_clear_hist.pack(side="right", padx=5)
 
# Keep the window open and running
root.mainloop()