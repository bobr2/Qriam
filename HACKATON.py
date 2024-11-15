import csv
import pandas as pd

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


print(arr_s)
print(arr_h)
print(arr_d)

def for_work(arr):
    arr = arr[arr["status"] == "Создано"]
    digital = pd.to_numeric(arr["estimation"], errors="raise").fillna(0)
    s_digit = sum([i for i in digital])
    return s_digit

print(for_work(arr_d))


def in_work(): pass
def made(): pass
def removed(): pass
def backlog_check():pass
def task_blocked(): pass
def excluded(): pass
def added(): pass
