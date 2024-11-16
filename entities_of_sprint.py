def ent(sprint,arr_s):
    entity=arr_s['entity_ids'].loc[sprint-1].replace('{','',1)
    entity=entity.replace('}','',1)
    entity=entity.split(',')
    entity=list(map(int,entity))
    return entity