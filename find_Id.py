

def ent(sprint,area,arr_s, arr_d): #Получаем id
    indx = arr_s["sprint_name"] == sprint
    entity= ((arr_s.loc[indx])['entity_ids'].values)[0]

    entit_ran = arr_d[arr_d["area"] == area]["entity_id"]


    entity = entity.replace('{','',1)
    entity=entity.replace('}','',1)
    entity=entity.split(',')
    entity=list(map(int,entity))

    inter = set(entit_ran) & set(entity)
    entity = list(inter)

    return entity

