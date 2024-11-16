import csv
import pandas as pd
from task import for_work, in_work

url_1 = "Sprints.csv" # Ему соответствует arr_s
url_2 = "History.csv" # Ему соответствует arr_h
url_3 = "Data.csv" # Ему соответствует arr_d

def read_file(url):
    with open(url, encoding="utf-8") as f:
        return pd.DataFrame([i for i in csv.reader(f, delimiter=";")][2:])

arr_s, arr_h, arr_d = read_file(url_1), read_file(url_2), read_file(url_3)

arr_s.columns = ("sprint_name", "sprint_status", "sprint_start", "sprint_end", "entity_ids")
arr_h.columns = ("entity_id", "history_property_name", "history_date", "history_version", "history_change_type", "history_change", "СТОЛБЕЦ")
arr_d.columns = ("entity_id", "area", "type",	"status", "state", "priority","ticket_number", "name", "create_date", "created_by",	"update_date",	"updated_by",	"parent_ticket_id",	"assignee",	"owner", "due_date", "rank",	"estimation",	"spent",	"workgroup",	 "resolution")

arr_h["entity_id"] = pd.to_numeric(arr_h["entity_id"], errors='raise')
arr_d["entity_id"] = pd.to_numeric(arr_d["entity_id"], errors='raise')


def get_history(entity_id, arr_h, arr_d):
    task = {"description": "",
            "estimation": "",
            "owner": "",
            "CтатусИзменения": "",
            "time": "",
            "resolution": ""
            }

    ind = arr_h["entity_id"] == entity_id

    for index, row in arr_h[ind].iterrows():

        if row.values[1] == "Статус":

            task["CтатусИзменения"] += '(' + row.values[-3] + ")"
            if row.values[1] != "":
                task["resolution"] = row.values[-3]

        if row.values[1] == "Исполнитель":
            task["owner"] = row.values[-3]

    kk = arr_d[arr_d["entity_id"] == entity_id]
    print(kk["estimation"])
    print()

    task["description"] = kk["name"]
    task["estimation"] = kk["estimation"]

    return task
# print(get_history(4449728, arr_h, arr_d))

if __name__ == "__main__":
    print(for_work(arr_d))
    print(in_work(arr_d))