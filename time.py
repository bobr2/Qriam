from datetime import datetime
from read_csv_3t import read_csv
arr_s, arr_h, arr_d=read_csv('Sprints.csv','History.csv','Data.csv')
def get_time(sprint,url_s):
    start_time_str=url_s['sprint_start'].loc[sprint-1]
    start_time=datetime.strptime(start_time_str,'%Y-%m-%d %H:%M:%S.%f')
    end_time_str=url_s['sprint_end'].loc[sprint-1]
    end_time=datetime.strptime(end_time_str,'%Y-%m-%d %H:%M:%S.%f')
    return start_time, end_time



