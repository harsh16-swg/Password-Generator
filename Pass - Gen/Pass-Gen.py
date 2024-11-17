import random
import string
import tkinter as tk
from tkinter import ttk, messagebox
import re


def password_strength(password):
    """
    Analyze the strength of a given password using regex for uppercase, lowercase, digits, and special characters.
    """
    # Initialize strength variables
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[@$!%*?&]', password))

    # Calculate strength
    strength = 0
    if length >= 8:
        strength += 1
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    # Determine strength level
    if strength <= 2:
        return "Weak"
    elif strength == 3:
        return "Moderate"
    else:
        return "Strong"


def generate_password():
    """
    Generate a password based on user input and display it in the GUI.
    """
    try:
        # Get length from user input
        length = int(length_entry.get())
        if length < 6:
            messagebox.showerror("Error", "Password length must be at least 6.")
            return

        # Get selected complexity level
        complexity = complexity_var.get()
        if complexity not in [1, 2, 3, 4]:
            messagebox.showerror("Error", "Select a valid complexity level.")
            return

        # Define character sets for each complexity level
        char_sets = {
            1: string.ascii_lowercase,  # Lowercase letters only
            2: string.ascii_lowercase + string.ascii_uppercase,  # Lowercase + Uppercase
            3: string.ascii_letters + string.digits,  # Letters + Digits
            4: string.ascii_letters + string.digits + string.punctuation,  # All characters
        }

        # Generate the password
        characters = char_sets[complexity]
        password = ''.join(random.choice(characters) for _ in range(length))
        password_output.set(password)  # Update the output field with the generated password

        # Analyze and display password strength
        strength = password_strength(password)
        strength_output.set(f"Strength: {strength}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the password length.")


# Create the main application window
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x400")
app.resizable(False, False)

# Title Label
title_label = tk.Label(app, text="Password Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Password Length Input
length_label = tk.Label(app, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(app, width=10)
length_entry.pack(pady=5)

# Complexity Selection
complexity_var = tk.IntVar(value=1)
complexity_label = tk.Label(app, text="Select Complexity Level:")
complexity_label.pack()

complexity_frame = ttk.Frame(app)
complexity_frame.pack(pady=5)

complexity_options = [
    ("Lowercase letters only", 1),
    ("Lowercase and uppercase letters", 2),
    ("Letters and digits", 3),
    ("Letters, digits, and special characters", 4),
]

for text, value in complexity_options:
    ttk.Radiobutton(complexity_frame, text=text, variable=complexity_var, value=value).pack(anchor=tk.W)

# Output Field
password_output = tk.StringVar()
output_label = tk.Label(app, text="Generated Password:")
output_label.pack(pady=10)
output_entry = tk.Entry(app, textvariable=password_output, state="readonly", width=30)
output_entry.pack()

# Strength Display
strength_output = tk.StringVar()
strength_label = tk.Label(app, textvariable=strength_output, font=("Arial", 12))
strength_label.pack(pady=5)

# Generate Button
generate_button = tk.Button(
    app,
    text="Generate Password",
    command=generate_password,
    bg="lightblue",
    fg="black",
    font=("Arial", 14),
    height=2,  # Bigger button height
    width=20   # Bigger button width
)
generate_button.pack(pady=20)

# Run the Application
app.mainloop()
