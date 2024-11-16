def Get_history(entity_id, arr_h, arr_d):

    task = {"description" : "",
            "estimation" : "",
            "owner" : [],
            "СтатусИзменения" : "",
            "time" : "",
            "status" : "",
            "DinamicStatus" : "",
            "спринт" : ""
            }
    
    ind = arr_h["entity_id"] == entity_id

    for index, row in arr_h[ind].iterrows():

        #print(f"Index: {index}, Values: {list(row.values)}")

        if row.values[1] == "Статус":
            task["СтатусИзменения"] += '('+ row.values[-3]+ ")"

            if row.values[1] != "":
                task["DinamicStatus"] == row.values[-3]

        if row.values[1] == "Исполнитель":
            for x in row.values[-3].split("->"):

                if "<empty>" not in x:
                    task["owner"].append(x.replace(" ", ""))


    ind1 = arr_d["entity_id"] == entity_id
    kk = arr_d[ind1].values.tolist()[0]

    task["status"] = kk[3]
    task["description"] = kk[7]
    task["estimation"] = kk[-4]
    return task