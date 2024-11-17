import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from tkinter import ttk
import csv
import pandas as pd

def graphics():
    def update_values(new_values):
        combo['values'] = new_values
        combo.current(0)

    def ok_clicked():
        selected_value = combo.get()
        data.append(selected_value)
        print(data)
    
    def select_file():
        global selected_file
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                   filetypes=(("CSV files", "*.csv"), ("Comma Separated Values", ".csv"),("all files", "*.*")))
        selected_file = Path(root.filename)
        data.append(selected_file)

        with open(selected_file, encoding="utf-8") as f:
            values = pd.DataFrame([i for i in csv.reader(f, delimiter=";")][2:])
            values.columns = ("sprint_name", "sprint_status", "sprint_start", "sprint_end", "entity_ids")
            options = list(values["sprint_name"].values)
            update_values(options)

    def select_file_hist_data():
        global selected_file
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                   filetypes=(("CSV files", "*.csv"), ("Comma Separated Values", ".csv"),("all files", "*.*")))
        selected_file = Path(root.filename)
        data.append(selected_file)

    def mainLOL():
        
        f = open("paths.txt", "w")
        for x in data:
            f.write(str(x))
            f.write("\n")
        root.destroy()


    root = tk.Tk()
    root.title("Файловое меню")

    label = tk.Label(root, text="Нажмите кнопку, чтобы выбрать файл.")
    label.pack(pady=10)

    button = tk.Button(root, text="Выбрать файл Sprint", command=select_file)
    button.pack(padx=1,pady=10)

    button = tk.Button(root, text="Выбрать файл History", command=select_file_hist_data)
    button.pack(padx=10,pady=10)

    button = tk.Button(root, text="Выбрать файл Data", command=select_file_hist_data)
    button.pack(padx=20,pady=10)

    ok_button = tk.Button(root, text="OK", command=ok_clicked)
    ok_button.pack(pady=(0, 10))


    options = ["Опция 1", "Опция 2", "Опция 3"]

    combo = ttk.Combobox(root, values=options)
    combo.current(0) 
    combo.pack(padx=20, pady=20)






    button1 = tk.Button(root, text="MAIN", command=mainLOL)
    button1.pack(pady=20)
    

    data = []
    url = []

    
    


    root.mainloop()