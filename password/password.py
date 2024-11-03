import string
import tkinter as tk
from tkinter import ttk, messagebox

# Function to check password strength
def check_password_strength(password):
    strength = 0
    lower_count = upper_count = num_count = special_count = 0

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        else:
            special_count += 1

    # Strength calculation
    if len(password) >= 8:
        strength += 1
    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    return strength

# Function to update UI dynamically based on password strength
def update_strength_bar(event):
    password = entry_password.get()
    strength = check_password_strength(password)

    # Update progress bar
    progress['value'] = strength * 20  # Multiply to fill bar

    # Change progress bar color and emoji dynamically
    if strength <= 2:
        progress['style'] = "red.Horizontal.TProgressbar"
        label_feedback.config(text="😕 Weak! Add uppercase, numbers, or special characters.", fg="red")
    elif strength == 3:
        progress['style'] = "yellow.Horizontal.TProgressbar"
        label_feedback.config(text="🙂 Decent! Try mixing upper and lower case letters.", fg="orange")
    elif strength == 4:
        progress['style'] = "green.Horizontal.TProgressbar"
        label_feedback.config(text="😎 Strong! Add a few special characters for extra security.", fg="green")
    elif strength == 5:
        progress['style'] = "blue.Horizontal.TProgressbar"
        label_feedback.config(text="💪🎉 Super Strong! Your password is secure!", fg="blue")

# Function for alert when user submits
def submit_password():
    password = entry_password.get()
    strength = check_password_strength(password)

    if strength < 3:
        messagebox.showwarning("Password Weak", "Your password is weak! Improve it for better security.")
    else:
        messagebox.showinfo("Password Strong", "Your password is strong!")

# Main GUI window setup with Dark theme
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("500x400+700+250")
window.configure(bg="#2b2b2b")  # Dark background

# Styling progress bar colors
style = ttk.Style()
style.theme_use('clam')
style.configure("red.Horizontal.TProgressbar", troughcolor='#333333', background='red')
style.configure("yellow.Horizontal.TProgressbar", troughcolor='#333333', background='orange')
style.configure("green.Horizontal.TProgressbar", troughcolor='#333333', background='green')
style.configure("blue.Horizontal.TProgressbar", troughcolor='#333333', background='blue')

# Labels and Entry
label_title = tk.Label(window, text="🔐 Enter Your Password", font=("Helvetica", 16), fg="white", bg="#2b2b2b")
label_title.pack(pady=15)

entry_password = tk.Entry(window, show="*", font=("Helvetica", 14), width=35)
entry_password.pack(pady=10)
entry_password.bind("<KeyRelease>", update_strength_bar)  # Event listener for live updates

# Progress Bar
progress = ttk.Progressbar(window, length=350, mode="determinate", style="red.Horizontal.TProgressbar")
progress.pack(pady=15)

# Feedback label
label_feedback = tk.Label(window, text="Start typing to check password strength...", font=("Helvetica", 12), fg="white", bg="#2b2b2b")
label_feedback.pack(pady=10)

# Submit Button
submit_button = tk.Button(window, text="🔍 Check Password", font=("Helvetica", 14), bg="gray", fg="white", command=submit_password)
submit_button.pack(pady=20)

# Run the application
window.mainloop()