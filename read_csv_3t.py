import csv
import pandas as pd

def read_csv(url_s, url_h, url_d): 
    

    def read_file(url):
        with open(url, encoding="utf-8") as f:
            return pd.DataFrame([i for i in csv.reader(f, delimiter=";")][2:])
    
    arr_s, arr_h, arr_d = read_file(url_s), read_file(url_h), read_file(url_d)


    arr_s.columns = ("sprint_name", "sprint_status", "sprint_start", "sprint_end", "entity_ids")
    arr_h.columns = ("entity_id", "history_property_name", "history_date", "history_version", "history_change_type", "history_change", "СТОЛБЕЦ", "hh")
    arr_d.columns = ("entity_id", "area", "type",	"status", "state", "priority","ticket_number", "name", "create_date", "created_by",	"update_date",	"updated_by",	"parent_ticket_id",	"assignee",	"owner", "due_date", "rank",	"estimation",	"spent",	"workgroup",	 "resolution")


    arr_h["entity_id"] = pd.to_numeric(arr_h["entity_id"], errors='raise')
    arr_d["entity_id"] = pd.to_numeric(arr_d["entity_id"], errors='raise')

    return arr_s, arr_h, arr_d