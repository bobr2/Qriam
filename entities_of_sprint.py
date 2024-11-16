def ent(sprint,arr_s):
    entity=arr_s['entity_ids'].loc[sprint-1].replace('{','',1)
    entity=entity.replace('}','',1)
    entity=entity.split(',')
    entity=list(map(int,entity))
    return entity

# На вход берет номер спринта (нумерация с 1) и таблицу спринтов.
# Выводит массив с задачами, которые относятся к данному спринту