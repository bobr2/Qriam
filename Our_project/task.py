import pandas as pd

def for_work(arr):
    arr = arr[arr["status"] == "Создано"]
    digital = pd.to_numeric(arr["estimation"], errors="raise").fillna(0)
    s_digit = sum([i/3600 for i in digital])
    return s_digit


def in_work(arr):
    arr = arr[arr["status"] != "Закрыто"]
    arr = arr[arr["status"] != "Выполнено"]

    digital = pd.to_numeric(arr["estimation"], errors="raise").fillna(0)
    s_digit = sum([i/3600 for i in digital])
    return s_digit


def made(): pass
def removed(): pass
def backlog_check():pass
def task_blocked(): pass
def excluded(): pass
def added(): pass