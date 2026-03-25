print("FILE INTEGRITY CHECKER WITH GUI TOOL")

import hashlib
import tkinter as tk
from tkinter import filedialog
from colorama import init, Fore

init(autoreset=True)

# ------------------- Hash Function -------------------
def calculate_hash(file_path):
    hash_algo = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hash_algo.update(chunk)
        return hash_algo.hexdigest()
    except FileNotFoundError:
        return None

# ------------------- GUI Functions -------------------
def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def generate_hash():
    file_path = file_entry.get()
    hash_value = calculate_hash(file_path)
    output_panel.config(state='normal')
    output_panel.delete("1.0", tk.END)
    if hash_value:
        output_panel.insert(tk.END, hash_value)
    else:
        output_panel.insert(tk.END, "File not found!")
    output_panel.config(state='disabled')

# ------------------- GUI Setup -------------------
root = tk.Tk()
root.title("SHA-256 File Hasher - Hacker Style")
root.geometry("700x400")
root.configure(bg="black")

# Title
tk.Label(root, text="SHA-256 File Hash Generator", bg="black", fg="lime", font=("Consolas", 16)).pack(pady=10)

# File Entry + Browse
file_entry = tk.Entry(root, width=80, bg="black", fg="lime", insertbackground="lime")
file_entry.pack(pady=5)

tk.Button(root, text="Browse File", command=browse_file, bg="gray20", fg="lime").pack(pady=5)

# Generate Button
tk.Button(root, text="Generate Hash", command=generate_hash, bg="red", fg="white").pack(pady=10)

# Output Panel
output_panel = tk.Text(root, height=10, width=80, bg="black", fg="lime", font=("Consolas", 12))
output_panel.pack(pady=10)
output_panel.config(state='disabled')

root.mainloop()
