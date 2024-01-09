import os
import tkinter as tk
from tkinter import filedialog
import subprocess

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")
        
        self.create_widgets()

    def create_widgets(self):
        self.file_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.file_listbox.pack(expand=tk.YES, fill=tk.BOTH)

        self.load_files(os.getcwd())

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        btn_open = tk.Button(button_frame, text="Open", command=self.open_file)
        btn_open.pack(side=tk.LEFT, padx=5)

        btn_refresh = tk.Button(button_frame, text="Refresh", command=self.refresh_files)
        btn_refresh.pack(side=tk.LEFT, padx=5)

    def load_files(self, path):
        self.file_listbox.delete(0, tk.END)
        files = os.listdir(path)
        for file in files:
            self.file_listbox.insert(tk.END, file)

    def open_file(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            selected_file = self.file_listbox.get(selected_index[0])
            file_path = os.path.join(os.getcwd(), selected_file)
            if os.path.isdir(file_path):
                self.load_files(file_path)
            else:
                self.open_file_directly(file_path)

    def open_file_directly(self, file_path):
        try:
            subprocess.run(["xdg-open", file_path])  
        except FileNotFoundError:
            try:
                subprocess.run(["open", file_path])  
            except FileNotFoundError:
                try:
                    subprocess.run(["start", " ", file_path], shell=True)  
                except FileNotFoundError:
                    print("Unable to open the file. Please open it manually.")

    def refresh_files(self):
        current_path = os.getcwd()
        self.load_files(current_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()
