import csv

class AiDataSet:
    data:list

    def __init__(self):
        
        file_path="object_oriented_programming\\AI_Impact\\AI_Impact_on_Jobs_2030 (1).csv"

        fr= open(file_path,"r",encoding="utf-8")

        reader=csv.DictReader(fr)

        self.data=[row for row in reader]

    def total_records(self):

        print(len(self.data))

    def first_record(self):

        print(self.data[0])

ai_instance=AiDataSet()

ai_instance.total_records()
ai_instance.first_record()