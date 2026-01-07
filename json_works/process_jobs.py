from json import load

file_path ="json_works\\jobs.json"

fr = open(file_path,"r",encoding="utf-8")

data = load(fr)

print(len(data))