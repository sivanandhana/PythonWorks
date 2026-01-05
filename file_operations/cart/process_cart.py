file_path="file_operations\\cart\\cart_items_100.csv"

fr=open(file_path,"r",encoding="utf-8")

import csv

reader=csv.DictReader(fr)

data=[row for row in reader]

# print(len(data))

order_summary={}

for o in data:

    title=o.get("title")
    qty=int(o.get("quantity"))

    if title in order_summary:

        order_summary[title]+=qty
    else:
        order_summary[title]=qty

# print(order_summary)

maximum=max(order_summary.values())


max_items=[k for k,v in order_summary.items()if v==maximum]

print(max_items)


minimum=min(order_summary.values())

min_items=[k for k,v in order_summary.items() if v==minimum]

print(min_items)