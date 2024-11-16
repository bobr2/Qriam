#4449728
from get_history import Get_history
from Analys import ent
import csv
import pandas as pd
from read_csv_3t import read_csv
from Frontend import graphics

graphics() #frotnend

data = [] # Грузим файлы
f = open("paths.txt", "r")
for x in f.readlines():
    data.append(x[:-1])
print(data)
arr_s, arr_h, arr_d = read_csv(*data)

ids = ent(1,arr_s)

for i in ids:
    for a,b in Get_history(i, arr_h, arr_d).items():
           if b != "":
            print(f"{a}: {b}")
    

