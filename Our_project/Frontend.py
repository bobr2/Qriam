import tkinter as tk
from tkinter import filedialog
from pathlib import Path



def graphics():
    
    def select_file():
        global selected_file
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                   filetypes=(("text files", "*.txt"), ("CSV files", "*.csv"), ("Comma Separated Values", ".csv"),("all files", "*.*")))
        selected_file = Path(root.filename)
        url.append(selected_file)

    def mainLOL():
        data = url
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
    button = tk.Button(root, text="Выбрать файл History", command=select_file)
    button.pack(padx=10,pady=10)
    button = tk.Button(root, text="Выбрать файл Data", command=select_file)
    button.pack(padx=20,pady=10)

    button1 = tk.Button(root, text="MAIN", command=mainLOL)
    button1.pack(pady=20)
    
    flag = False
    data = []
    url = []

    
    


    root.mainloop()

graphics()