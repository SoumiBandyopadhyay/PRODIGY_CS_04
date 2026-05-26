import tkinter as tk
from datetime import datetime

LOG_FILE = "key_log.txt"

def log_key(event):
    key = event.keysym

    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.now()} - {key}\n")

    label.config(text=f"Last Key Pressed: {key}")

# Create window
root = tk.Tk()
root.title("Keyboard Event Logger")
root.geometry("400x200")

label = tk.Label(root, text="Press any key...", font=("Arial", 14))
label.pack(pady=50)

# Bind keyboard events only to this app window
root.bind("<Key>", log_key)

root.mainloop()
