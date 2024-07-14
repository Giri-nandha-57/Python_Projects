import tkinter as tk
from tkinter import filedialog, messagebox
import json

# Function to load script from a file
def load_script():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            script_text.delete('1.0', tk.END)
            script_text.insert(tk.END, file.read())

# Function to process the script into scenes and actions
def process_script():
    script = script_text.get('1.0', tk.END).strip()
    if script:
        scenes = []
        lines = script.split('\n')
        current_scene = []
        
        for line in lines:
            line = line.strip()
            if not line:
                if current_scene:
                    scenes.append(current_scene)
                    current_scene = []
            else:
                current_scene.append(line)
        
        if current_scene:
            scenes.append(current_scene)

        scenes_list.delete(0, tk.END)
        for i, scene in enumerate(scenes, 1):
            scenes_list.insert(tk.END, f"Scene {i}")
            for action in scene:
                scenes_list.insert(tk.END, f"  - {action}")
    else:
        messagebox.showwarning("Warning", "The script cannot be empty.")

# Function to save the processed data to a file
def save_processed_data():
    processed_data = {
        "script": script_text.get('1.0', tk.END).strip(),
        "scenes": [scenes_list.get(i) for i in range(scenes_list.size())]
    }
    with open('Processed_Script/Script_Scene.json', 'w') as file:
        json.dump(processed_data, file)

# Setting up the Tkinter window
root = tk.Tk()
root.title("Story Script Processor")

# Text widget for entering the script
script_text = tk.Text(root, height=25, width=100)
script_text.grid(row=0, column=0, columnspan=3)

# Buttons to load and process the script
load_button = tk.Button(root, text="Load Script in .txt", command=load_script)
load_button.grid(row=1, column=0)

process_button = tk.Button(root, text="Process The Script", command=process_script)
process_button.grid(row=1, column=1)

# Listbox to display the processed scenes and actions
scenes_list = tk.Listbox(root, width=100, height=15)
scenes_list.grid(row=2, column=0, columnspan=3)

# Set up window close protocol to save processed data
root.protocol("WM_DELETE_WINDOW", save_processed_data)

# Run the application
root.mainloop()
