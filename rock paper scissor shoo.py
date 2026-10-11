import tkinter as tk
import random
 
# Core game logic function
def play_game(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win! 🎉"
    else:
        result = "Computer Wins! 😭"
        
    # Update UI text labels with results
    user_label.config(text=f"Your Choice: {user_choice}")
    computer_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result)
 
# Initialize the main Tkinter window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x350")
root.resizable(False, False)
 
# Main title label
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 18, "bold"), pady=10)
title_label.pack()
 
# Instruction label
instruction_label = tk.Label(root, text="Choose your move:", font=("Helvetica", 12))
instruction_label.pack(pady=5)
 
# Frame container for control buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
 
# Rock, Paper, and Scissors buttons linked to the game logic function
rock_button = tk.Button(button_frame, text="Rock", font=("Helvetica", 12), width=10, bg="#f0a500", fg="white", command=lambda: play_game("Rock"))
rock_button.grid(row=0, column=0, padx=5)
 
paper_button = tk.Button(button_frame, text="Paper", font=("Helvetica", 12), width=10, bg="#007acc", fg="white", command=lambda: play_game("Paper"))
paper_button.grid(row=0, column=1, padx=5)
 
scissors_button = tk.Button(button_frame, text="Scissors", font=("Helvetica", 12), width=10, bg="#d9534f", fg="white", command=lambda: play_game("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)
 
# Labels to display choices made during the round
user_label = tk.Label(root, text="Your Choice: -", font=("Helvetica", 12), pady=5)
user_label.pack()
 
computer_label = tk.Label(root, text="Computer's Choice: -", font=("Helvetica", 12), pady=5)
computer_label.pack()
 
# Bold label to display final match result
result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), fg="#333333", pady=15)
result_label.pack()
 
# Start the Tkinter application loop
root.mainloop()