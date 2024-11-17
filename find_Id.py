



def ent(sprint,table): #Получаем id
    indx = table["sprint_name"] == sprint
    entity= ((table.loc[indx])['entity_ids'].values)[0]


    entity = entity.replace('{','',1)
    entity=entity.replace('}','',1)
    entity=entity.split(',')
    entity=list(map(int,entity))

    return entity

