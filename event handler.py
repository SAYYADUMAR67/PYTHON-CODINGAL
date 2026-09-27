from tkinter import *
window = Tk()
window.title("Event Handler Example")
window.geometry("400x200")
def handle_keypress(event):
    '''print the character associated with the key pressed'''
    print(event.char)
window.bind("<Key>", handle_keypress)
def handle_button_click():
    '''print a message when the button is clicked'''
    print("Button was clicked!")
button = Button(window, text="Click Me!", command=handle_button_click)
button.pack()
button.bind("<Button-1>", handle_button_click)
window.mainloop()