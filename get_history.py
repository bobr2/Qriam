from Get_time import get_time
import pandas as pd


def get_history(entity_id, sprint, arr_s, arr_h, arr_d,): #Получает номер задачи и интересующий нас спринт + массивы

    task = {"description" : "",
            "estimation" : "",
            "owner" : [],
            "status_in_sprint" : "",
            "status" : "",
            "resolution" : "",
            "type" : "",
            "sprint" : "",
            "time_sprint" : ""
            }
    
    start, end = get_time(sprint, arr_s)

    ind = arr_h["entity_id"] == entity_id

    for index, row in arr_h[ind].iterrows():

        time = pd.to_datetime(row.values[2], format='%m/%d/%y %H:%M')
        #print(f"Index: {index}, Values: {list(row.values)}")
        if time <= end:
            if row.values[1] == "Спринт" and row.values[-3] != "":
                task["sprint"] = row.values[-3].replace("->", "|").split("|")[1][1:]
                task["time_sprint"] = time
        if start <= time <= end:

            if row.values[1] == "Статус":
                task["status_in_sprint"] =row.values[-3].split("->")[1][1:]

            elif row.values[1] == "Оценка" and row.values[-3] != "":
                task["estimation"] = int(row.values[-3].replace("->", "|").split("|")[1][1:])
            
            elif row.values[1] == "Резолюция" and row.values[-3] != "":
                task["resolution"] = row.values[-3].replace("->", "|").split("|")[1][1:]
            """
            elif row.values[1] == "Спринт" and row.values[-3] != "":
                task["sprint"] = row.values[-3].replace("->", "|").split("|")[1][1:]
                task["time_sprint"] = row.values[2]
            """




            

            if row.values[1] == "Исполнитель":
                for x in row.values[-3].split("->"):

                    if "<empty>" not in x:
                        task["owner"].append(x.replace(" ", ""))


    ind1 = arr_d["entity_id"] == entity_id
    kk = arr_d[ind1].values.tolist()[0]

    task["status"] = kk[3]
    task["description"] = kk[7]
    task["type"] = kk[2]

    if task["resolution"] == "":
        task["resolution"] = kk[-1]
        

    if task["estimation"] == "":
        if kk[-4] != "":
            task["estimation"] = int(kk[-4])
        else:
            task["estimation"] = 0
    
    if task["status_in_sprint"] == "":
        task["status_in_sprint"] = "Создано"
    
    nazv = {"closed": "Закрыто", "InProgress":"В работе", "created":"Создано", "done": "Выполнено", "closed":"Закрыто"}

    if task["status_in_sprint"] in nazv.keys():
        task["status_in_sprint"] = nazv[task["status_in_sprint"]]
    

    return task