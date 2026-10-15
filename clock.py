
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.configure(bg="black")

def update_time():
    time_label.config(text=strftime("%H:%M:%S %p"))
    time_label.after(1000, update_time)

time_label = tk.Label(
    root,
    font=("Arial", 40, "bold"),
    background="black",
    foreground="cyan"
)
time_label.pack(expand=True)

update_time()
root.mainloop()
