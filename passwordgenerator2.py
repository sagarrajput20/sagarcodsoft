import tkinter as tk
import string
import random

def generate_password():
    password_length = int(length_entry.get())
    if password_length < 6:
        password_label.config(text="Password length should be at least 6 characters.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        password_label.config(text="Generated Password: " + password)

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()
