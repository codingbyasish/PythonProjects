import xml.etree.ElementTree as ET

import tkinter as tk

from tkinter import messagebox

# Function to find the value of a specific tag

def get_tag_value(root, tag_name):

    # Find the first occurrence of the tag

    element = root.find('.//' + tag_name)

    if element is not None:

        return element.text

    else:

        return None

# Function to handle button click event

def search_tag():

    tag_name = entry.get()

    tag_value = get_tag_value(root, tag_name)

    if tag_value is not None:

        messagebox.showinfo("Tag Value", f"The value of the tag '{tag_name}' is: {tag_value}")

    else:

        messagebox.showwarning("Tag Not Found", f"The tag '{tag_name}' was not found in the XML file.")

# Create a Tkinter window

window = tk.Tk()

window.title("XML Tag Value Search")

# Create a label and entry widget for tag name

label = tk.Label(window, text="Enter tag name:")

label.pack(pady=5)

entry = tk.Entry(window, width=30)

entry.pack(pady=5)

# Create a search button

search_button = tk.Button(window, text="Search", command=search_tag)

search_button.pack(pady=5)

# Parse the XML file

tree = ET.parse('C:/Windows/Professional.xml')

root = tree.getroot()

# Run the Tkinter event loop

window.mainloop()