import tkinter as tk
from tkinter import ttk
import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_passwords():
    length = int(length_entry.get())
    count = int(count_entry.get())
    passwords = [generate_password(length) for _ in range(count)]
    result_text.set('\n'.join(passwords))

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Create and configure main frame
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

# Length Label and Entry
ttk.Label(main_frame, text="Password Length:").grid(column=0, row=0, sticky=tk.W)
length_entry = ttk.Entry(main_frame)
length_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

# Count Label and Entry
ttk.Label(main_frame, text="Number of Passwords:").grid(column=0, row=1, sticky=tk.W)
count_entry = ttk.Entry(main_frame)
count_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

# Generate Passwords Button
generate_button = ttk.Button(main_frame, text="Generate Passwords", command=generate_passwords)
generate_button.grid(column=0, row=2, columnspan=2)

# Result Text
result_text = tk.StringVar()
result_label = ttk.Label(main_frame, text="Generated Passwords:")
result_label.grid(column=0, row=3, sticky=tk.W)
result_display = ttk.Label(main_frame, textvariable=result_text, wraplength=400, justify=tk.LEFT)
result_display.grid(column=0, row=4, columnspan=2, sticky=tk.W)

# Run the GUI
root.mainloop()
