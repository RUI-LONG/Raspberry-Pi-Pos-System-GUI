import json

def read_json(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def write_json(data, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, sort_keys=False)