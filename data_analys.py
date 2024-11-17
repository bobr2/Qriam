from find_Id import ent
from read_csv_3t import read_csv
from get_history import get_history
from datetime import date, datetime, timedelta
from Get_time import get_time

arr_s, arr_h, arr_d = read_csv('Sprints.csv', 'History.csv', 'Data.csv')


def rates(sprint, arr_s, arr_h, arr_d):
    start, end = get_time(sprint, arr_s)
    entit = ent(sprint, arr_s)
    summ = 0
    rate = {'for_exect': 0,
            'in_work': 0,
            'done': 0,
            'removed': 0,
            'backlog_change': 0
            }
    twodays = start_of_sprint = 0
    for id in entit:
        hist = get_history(id, sprint, arr_s, arr_h, arr_d)
        if hist['status_in_sprint'] == 'Создано':
            pl = hist['estimation']
            rate['for_exect'] += pl
        if hist['status_in_sprint'] != 'Сделано' or hist['status_in_sprint'] != 'Снято':
            pl = hist['estimation']
            rate['in_work'] += pl
        if hist['status_in_sprint'] in ['Закрыто', 'Выполнено']:
            if hist['resolution'] in ['Отклонено', 'Отменено инициатором', 'Дубликат', 'Отклонен исполнителем ']:
                pl = hist['estimation']
                rate['removed'] += pl
        if hist['status_in_sprint'] in ['Закрыто', 'Выполнено']:
            pl = hist['estimation']
            rate['done'] += pl
        if hist['type']!='Дефект':
            if hist['time_sprint'] == '':
                start_of_sprint += hist['estimation']
            elif hist['time_sprint'] - start < timedelta(days=2):
                start_of_sprint += hist['estimation']
            else:
                twodays += hist['estimation']
    rate['done'] -= rate['removed']
    rate1 = {k: v/3600 for k, v in rate.items()}
    rate1['backlog_change']=(twodays/start_of_sprint)*100

    return rate1


