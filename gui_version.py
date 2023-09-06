import tkinter as tk
from common import fetch_crime_stats_for_postcode, fetch_postcode_from_zoopla

def fetch_data():
    input_data = entry.get()
    
    if "zoopla.co.uk" in input_data:
        postcode = fetch_postcode_from_zoopla(input_data)
        if not postcode:
            result.set("Failed to retrieve postcode from the URL.")
            return
    else:
        postcode = input_data

    stats, lat_lon = fetch_crime_stats_for_postcode(postcode)
    if stats and lat_lon:
        result.set(f"Latitude and Longitude: {lat_lon}\n"
                   f"In the last 12 months, there are {stats['crime_count']} crimes in the area.\n"
                   f"The most frequent crimes are {stats['top_three_frequent_crime']}\n"
                   f"The most frequent street is {stats['most_frequent_street']}\n"
                   f"The number of crimes in the last 12 months are:\n"
                   f"{stats['monthly_crime_count']}")
    else:
        result.set("Unable to fetch data.")

def run_gui_version():
    # Create and configure the main window
    root = tk.Tk()
    root.title("Zoopla Crime Stats")
    root.configure(bg='white')

    # Create and configure the input field
    global entry
    entry = tk.Entry(root, width=50, bg='white')
    entry.pack(pady=10)
    entry.insert(0, "Enter postcode or Zoopla URL here")

    # Create and configure the button
    button = tk.Button(root, text="Fetch Data", command=fetch_data, bg='white')
    button.pack(pady=10)

    # Create and configure the label to display results
    global result
    result = tk.StringVar()
    result.set("Results will be displayed here")
    label = tk.Label(root, textvariable=result, bg='white', justify='left')
    label.pack(pady=10)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    run_gui_version()
