import tkinter as tk
from tkinter import ttk

# Variables to store current selections
road_type_selection = None
weather_selection = None
time_selection = None


def open_ui():
    global road_type_selection, weather_selection, time_selection

    # Initialize the Tkinter window
    root = tk.Tk()
    root.title("Control Panel")
    root.geometry("300x250+1200+100")
    root.wm_attributes("-topmost", True)
    # Dropdown for road type
    road_type_label = tk.Label(root, text="Road Type:")
    road_type_label.pack(pady=(10, 0))

    road_type_options = ["Start", "Road", "Highway", "Dirt road", "Mountain pass", "Gravel road", "End"]
    road_type_var = tk.StringVar(value=road_type_options[0])
    road_type_dropdown = ttk.Combobox(root, textvariable=road_type_var, values=road_type_options)
    road_type_dropdown.pack(pady=5)

    # Dropdown for weather
    weather_label = tk.Label(root, text="Weather:")
    weather_label.pack(pady=(10, 0))

    weather_options = ["Clear", "Drizzle", "Storm", "Fog", "Snow"]
    weather_var = tk.StringVar(value=weather_options[0])
    weather_dropdown = ttk.Combobox(root, textvariable=weather_var, values=weather_options)
    weather_dropdown.pack(pady=5)

    # Dropdown for time (hour only, from 0 to 24)
    time_label = tk.Label(root, text="Hour of the Day:")
    time_label.pack(pady=(10, 0))

    time_options = [str(hour) for hour in range(25)]
    time_var = tk.StringVar(value=time_options[0])
    time_dropdown = ttk.Combobox(root, textvariable=time_var, values=time_options)
    time_dropdown.pack(pady=5)

    # Update global variables when a selection is made
    def update_selections():
        global road_type_selection, weather_selection, time_selection
        road_type_selection = road_type_var.get()
        weather_selection = weather_var.get()
        time_selection = time_var.get()

    # Bind selection updates
    road_type_dropdown.bind("<<ComboboxSelected>>", lambda e: update_selections())
    weather_dropdown.bind("<<ComboboxSelected>>", lambda e: update_selections())
    time_dropdown.bind("<<ComboboxSelected>>", lambda e: update_selections())

    # Run the Tkinter event loop
    root.mainloop()


def get_selections():
    # Function to return the current selections
    return {
        'road_type': road_type_selection,
        'weather': weather_selection,
        'time': time_selection
    }
