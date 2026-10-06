from tkinter import*

root = Tk()
root.title("main Window")
root.geometry("300x200")

def open_new_window():
    new_window = Toplevel(root)
    new_window.title("top level Window")
    new_window.geometry("200x150")
    Label(new_window, text="This is a new window").pack(pady=20)
    Button(new_window, text="Close", command=new_window.destroy).pack(pady=10)

Button(root, text="Open New Window", command=open_new_window).pack(pady=20)
root.mainloop()