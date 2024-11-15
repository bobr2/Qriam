def get_history(entity_id):
    
    task = {"description" : "",
            "estimation" : "",
            "owner" : "",
            "status" : "",
            "CтатусИзменения" : "",
            "time" : "",
            "wtf" : "",
            "resolution" : ""
            }
    
    ind = arr_h["entity_id"] == entity_id
    print(task.keys())
    for index, row in arr_h[ind].iterrows():
        print(f"Index: {index}, Values: {list(row.values)}")
        print(type(row.values[1]), row.values[-3])
        
        if row.values[1] == "Статус":
            print("vee")
            task["CтатусИзменения"] += '('+ row.values[-3]+ ")"
            if row.values[1] != "":
                task["status"] == row.values[-3]

        if row.values[1] == "Исполнитель":
            task["owner"] == row.values[-3]


    
    
    
    ind1 = arr_d["entity_id"] == entity_id
    kk = arr_d[ind1].to_dict()

    
    
    
    print(task.keys())
    print(task)


get_history(4449728)