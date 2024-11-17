#4449728
from get_history import get_history
from find_Id import ent
import csv
import pandas as pd
from read_csv_3t import read_csv
from Frontend import graphics
from data_analys import rates


graphics() #frotnend

data = [] # Грузим файлы
f = open("paths.txt", "r")
for x in f.readlines():
    data.append(x[:-1])
print(data)
"""
url_1 = "Sprints.csv" # Ему соответствует arr_s
url_2 = "History.csv" # Ему соответствует arr_h
url_3 = "Data.csv" # Ему соответствует arr_d
data=[url_1, url_2, url_3] 
"""
arr_s, arr_h, arr_d = read_csv(*data[:3])
sprint = data[-1]

#print(arr_d["owner"].unique())
#print(arr_d["created_by"].unique())
#print(arr_h["history_property_name"].unique())


print(rates(sprint, arr_s, arr_h, arr_d))


"""
#print(get_history(4449728, 1, arr_s, arr_h, arr_d)) 
for a,b in get_history(4449728, 1, arr_s,  arr_h, arr_d, ).items():
           if b != "":
            print(f"{a}: {b}")
"""
