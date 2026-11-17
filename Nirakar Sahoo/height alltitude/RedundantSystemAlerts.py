# Redundant System Alerts UI using Python (Tkinter)
# Run this file in VS Code using: python app.py

import tkinter as tk
from tkinter import ttk
import random
import time

# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("Redundant System Alerts")
root.geometry("700x500")
root.configure(bg="#0f172a")

title = tk.Label(
    root,
    text="Redundant System Monitoring Dashboard",
    font=("Arial", 22, "bold"),
    bg="#0f172a",
    fg="white"
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Safety Team Dashboard - Backup System Status",
    font=("Arial", 12),
    bg="#0f172a",
    fg="#cbd5e1"
)
subtitle.pack()

# -----------------------------
# Status Data
# -----------------------------
systems = {
    "Primary Flight Control": "Nominal",
    "Backup Navigation": "Nominal",
    "Battery Redundancy": "Warning",
    "Emergency Communication": "Nominal",
    "Sensor Network": "Critical",
}

status_colors = {
    "Nominal": "#22c55e",   # Green
    "Warning": "#facc15",   # Yellow
    "Critical": "#ef4444",  # Red
}

frames = {}

# -----------------------------
# Create System Cards
# -----------------------------
card_container = tk.Frame(root, bg="#0f172a")
card_container.pack(pady=30)

for system, status in systems.items():

    frame = tk.Frame(
        card_container,
        bg="#1e293b",
        bd=2,
        relief="ridge",
        padx=15,
        pady=15
    )
    frame.pack(fill="x", padx=20, pady=10)

    system_label = tk.Label(
        frame,
        text=system,
        font=("Arial", 14, "bold"),
        bg="#1e293b",
        fg="white"dir
    )
    system_label.pack(side="left")

    status_label = tk.Label(
        frame,
        text=status,
        font=("Arial", 13, "bold"),
        bg=status_colors[status],
        fg="black",
        padx=15,
        pady=5
    )
    status_label.pack(side="right")

    frames[system] = status_label

# -----------------------------
# Footer                                    
# -----------------------------
footer = tk.Label(
    root,
    text="All Systems Monitoring Active",
    font=("Arial", 11),
    bg="#0f172a",
    fg="#94a3b8"
)
footer.pack(side="bottom", pady=15)

# -----------------------------
# Simulate Live Monitoring
# -----------------------------
def update_status():
    possible_status = ["Nominal", "Warning", "Critical"]

    for system in systems:
        new_status = random.choice(possible_status)

        frames[system].config(
            text=new_status,
            bg=status_colors[new_status]
        )

    root.after(4000, update_status)

# Start auto-update
update_status()

# Run app
root.mainloop() 