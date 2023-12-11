import json
import tkinter as tk
from tkinter import filedialog
import os


def select_json_files():
    """ Open a file dialog to select JSON files """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_paths = filedialog.askopenfilenames(
        title='Select JSON Files',
        filetypes=[('JSON Files', '*.json')]
    )
    return root.tk.splitlist(file_paths)


def merge_json_files(file_paths):
    """ Merge multiple JSON files into a single JSON object """
    merged_data = {
        "type": "starjumpFleetviewer",
        "version": 1,
        "backgroundColor": "0c000000",
        "canvasZoom": "0.0372759372",
        "canvasPanX": "0.0000000000",
        "canvasPanY": "0.0000000000",
        "shipScaleFactor": "4.0000000000",
        "minZoom": "0.0010000000",
        "maxZoom": "1.0000000000",
        "canvasItems": []
    }

    for file_path in file_paths:
        with open(file_path, 'r') as file:
            data = json.load(file)
            merged_data["canvasItems"].extend(data.get("canvasItems", []))

    return merged_data


def main():
    files = select_json_files()
    if files:
        merged_json = merge_json_files(files)
        # Save in the same directory where the script is executed
        save_path = os.path.join(os.path.dirname(__file__), 'combinedfleet.json')
        with open(save_path, 'w') as outfile:
            json.dump(merged_json, outfile, indent=4)
        print(f"Merged JSON file created at '{save_path}'")
    else:
        print("No files selected.")


if __name__ == "__main__":
    main()
