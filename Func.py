def get_history(entity_id, arr_h, arr_d):
    
    task = {"description" : "",
            "estimation" : "",
            "owner" : "",
            "CтатусИзменения" : "",
            "time" : "",
            "resolution" : ""
            }
    
    ind = arr_h["entity_id"] == entity_id

    for index, row in arr_h[ind].iterrows():

        
        if row.values[1] == "Статус":

            task["CтатусИзменения"] += '('+ row.values[-3]+ ")"
            if row.values[1] != "":
                task["resolution"] == row.values[-3]

        if row.values[1] == "Исполнитель":
            task["owner"] == row.values[-3]


    
    
    
    ind1 = arr_d["entity_id"] == entity_id
    kk = arr_d[ind1].to_dict()


    task["description"] = kk["name"]
    task["estimation"] == kk["estimation"]
    
    

    return task


print(get_history(4449728))