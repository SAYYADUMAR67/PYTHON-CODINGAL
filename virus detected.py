import tkinter as tk
from tkinter import messagebox
 
def start_scan():
    messagebox.showinfo(
        "Scan Status", 
        "System scan initialized...\nScanning local drives (C:)..."
    )
    
    messagebox.showwarning(
        "WARNING!", 
        "Threat Detected!\nTrojan.Generic.7726 found in System32!"
    )
    
    user_choice = messagebox.askyesno(
        "Critical Choice", 
        "The virus is attempting to delete files.\nWould you like to isolate the threat?"
    )
    
    if user_choice:
        messagebox.showinfo(
            "Success", 
            "Threat successfully quarantined! Your system is safe."
        )
    else:
        messagebox.showerror(
            "CRITICAL ERROR", 
            "System override failed! Files are melting!\n\n(Just kidding, your system is perfectly fine!)"
        )

root = tk.Tk()
root.title("Matrix Security Scanner v1.0")
root.geometry("350x200")
root.configure(bg="#1e1e1e")  
 
title_label = tk.Label(
    root, 
    text="SYSTEM SECURITY SCANNER", 
    font=("Arial", 14, "bold"), 
    fg="#00ff00", 
    bg="#1e1e1e"
)
title_label.pack(pady=20)
 
scan_button = tk.Button(
    root, 
    text="START FULL SCAN", 
    font=("Arial", 11, "bold"),
    fg="white", 
    bg="#ff3333", 
    activebackground="#cc0000",
    activeforeground="white",
    command=start_scan,
    padx=10,
    pady=5
)
scan_button.pack(pady=20)
 
root.mainloop()
