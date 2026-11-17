import tkinter as tk
import random

root = tk.Tk()
root.title("Redundant System Alerts")
root.geometry("600x400")
root.configure(bg="black")

title = tk.Label(
    root,
    text="All Systems Nominal",
    font=("Arial", 24, "bold"),
    bg="black",
    fg="green"
)
title.pack(pady=40)

systems = [
    "Backup Navigation",
    "Battery System",
    "Emergency Sensors",
    "Flight Controller"
]

labels = []

for system in systems:
    frame = tk.Frame(root, bg="gray20", padx=10, pady=10)
    frame.pack(fill="x", padx=20, pady=10)

    name = tk.Label(
        frame,
        text=system,
        font=("Arial", 14),
        bg="gray20",
        fg="white"
    )
    name.pack(side="left")

    status = tk.Label(
        frame,
        text="Nominal",
        font=("Arial", 12, "bold"),
        bg="green",
        fg="black",
        padx=10
    )
    status.pack(side="right")

    labels.append(status)

def update_status():
    states = [
        ("Nominal", "green"),
        ("Warning", "yellow"),
        ("Critical", "red")
    ]

    for label in labels:
        text, color = random.choice(states)
        label.config(text=text, bg=color)

    root.after(3000, update_status)

update_status()

root.mainloop()