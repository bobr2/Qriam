
import csv
import pandas as pd

url_1 = "Sprints.csv" # Ему соответствует arr_s
url_2 = "History.csv" # Ему соответствует arr_h
url_3 = "Data.csv" # Ему соответствует arr_d


with open(url_1, encoding="utf-8") as f: arr_s = pd.DataFrame([i for i in csv.reader(f, delimiter=";")][2:])
with open(url_2, encoding="utf-8") as f: arr_h = pd.DataFrame([i for i in csv.reader(f, delimiter=";")][2:])
with open(url_3, encoding="utf-8") as f: arr_d = pd.DataFrame([i for i in csv.reader(f, delimiter=";")][2:])


arr_s.columns = ("sprint_name", "sprint_status", "sprint_start", "sprint_end", "entity_ids")
arr_h.columns = ("entity_id", "history_property_name", "history_date", "history_version", "history_change_type", "history_change")
arr_d.columns = ("entity_id", "area", "type",	"status", "state", "priority","ticket_number", "name", "create_date", "created_by",	"update_date",	"updated_by",	"parent_ticket_id",	"assignee",	"owner", "due_date", "rank",	"estimation",	"spent",	"workgroup",	 "resolution")



print(arr_s)
print(arr_h)
print(arr_d)
