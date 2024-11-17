from find_Id import ent
from read_csv_3t import read_csv
from get_history import get_history
from datetime import date, datetime, timedelta
from Get_time import get_time

arr_s, arr_h, arr_d = read_csv('Sprints.csv', 'History.csv', 'Data.csv')


def rates(sprint, arr_s,area, arr_h, arr_d):
    start, end = get_time(sprint, arr_s)
    entit = ent(sprint,area, arr_s,arr_d)
    summ = tasks = 0
    rate = {'for_exect': 0,
            'in_work': 0,
            'done': 0,
            'removed': 0,
            'backlog_change': 0
            }
    twodays = start_of_sprint = 0
    for id in entit:
        hist = get_history(id, sprint, arr_s, arr_h, arr_d)
        summ += hist['estimation']
        if hist['status_in_sprint'] == 'Создано':
            pl = hist['estimation']
            rate['for_exect'] += pl
            tasks += 1
        if hist['status_in_sprint'] in ['Закрыто', 'Выполнено']:
            if hist['resolution'] in ['Отклонено', 'Отменен инициатором', 'Дубликат', 'Отклонен исполнителем']:
                pl = hist['estimation']
                rate['removed'] += pl
                tasks += 1
        if hist['status_in_sprint'] in ['Закрыто', 'Выполнено']:
            pl = hist['estimation']
            rate['done'] += pl
            tasks += 1
        if hist['type'] != 'Дефект':
            if hist['time_sprint'] == '':
                start_of_sprint += hist['estimation']
            elif hist['time_sprint'] - start < timedelta(days=2):
                start_of_sprint += hist['estimation']
            else:
                twodays += hist['estimation']
    rate['done'] -= rate['removed']
    rate['in_work'] = summ - rate['done'] - rate['removed']
    rate1 = {k: v / 3600 for k, v in rate.items()}
    rate1['backlog_change'] = (twodays / start_of_sprint) * 100

    summ = sum(rate1.values())
    per = {'for_exect': 0,
           'in_work': 0,
           'done': 0,
           'removed': 0,
           'backlog_change': rate1['backlog_change']
           }
    for i in ['for_exect', 'in_work', 'done', 'removed']:
        per[i] = (rate1[i] / summ) * 100
    return per


def comp_sp(sprint, arr_s,area, arr_h, arr_d):
    summary={'for_exect': 0,
             'removed': 0,
             'backlog_change': 0
             }
    rate=rates(sprint, arr_s,area, arr_h, arr_d)
    if rate['for_exect']>20:
        summary['for_exect']=0
    elif 15<rate['for_exect']<=20:
        summary['for_exect']=1
    else:
        summary['for_exect']=2
    if rate['removed']>10:
        summary['removed']=0
    elif 7<rate['removed']<=10:

        summary['removed']=1
    else:
        summary['removed']=2
    if rate['backlog_change']>20:
        summary['backlog_change']=0
    elif 15<rate['backlog_change']<=20:
        summary['backlog_change']=1
    else:
        summary['backlog_change']=2

    return summary

