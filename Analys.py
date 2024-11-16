



def ent(sprint,table): #Получаем id
    entity=table['entity_ids'].loc[sprint-1].replace('{','',1)
    entity=entity.replace('}','',1)
    entity=entity.split(',')
    entity=list(map(int,entity))
    return entity

