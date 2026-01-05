file_path="file_operations\\titanic\\titanic_dataset.csv"

fr=open(file_path,"r")

# row=fr.readline()

# print(row)

# for line in fr:

#     lst=line.rstrip("\n").split(",")

   
    # line=line.split(",")[3].lstrip('"')

    # print(line)

    # id=line.split(",")[0]

    # id=lst[0]

    # survived=lst[1]

    # pclass=lst[2]

    # name=lst[3].lstrip('"')

    # gender=lst[5]

    # age=lst[6]

    # sib_sp=lst[7]

    # parch=lst[8]

    # fare=lst[10]

    # cabin=lst[11]

    # embarked=lst[12]


    # print(id,name,age,sib_sp,cabin)

import csv

reader=csv.DictReader(fr)

data=[row  for row in reader]

# print(data)


passengers_name=[dic.get("Name")for dic in data ]

# print(passengers_name)

# genders=[p.get("Sex") for p in data ]

# male_count=genders.count("male")

# female_count=genders.count("female")

# print("Total male passengers count : ",male_count)

# print("Total female passengers count : ",female_count)

survived_unsurvived=[p.get("Survived") for p in data ]

# print(survived_unsurvived)
# print("survived count : ",survived_unsurvived.count("1"))

# print("unsurvived count : ",survived_unsurvived.count("0"))


genders=[p.get("Sex") for p in data ]

# print("male count : ",genders.count('male'))

# print("female count : ",genders.count('female'))

all_class=[p.get("Pclass")for p in data]

# class_count={c:all_class.count(c)for c in all_class}

# print(class_count)

ages=[int(p.get("Age"))for p in data if p.get("Age").isdigit()]

youngest_age=min(ages)

oldest_age=max(ages)

# print("youngest age :",youngest_age)

# print("oldest age :",oldest_age)

first_ten=data[:11]

first_ten_name=[p.get("Name")for p in first_ten]

# print(first_ten_name)

boarding_station=[p.get("Embarked")for p in data if len(p.get("Embarked"))>0]

boarding_count={s:boarding_station.count(s)for s in boarding_station}

# print(boarding_count)

child_passengers=[p for p in data  if p.get("Age").isdigit() and int(p.get("Age"))<10 ]

# print(len(child_passengers))

survived_children=[p for p in child_passengers if p.get("Survived")=="1"]

# print(len(survived_children))


total_passengers=len(data)

# print(total)

survived_passengers=[p for p in data if p.get("Survived")=="1"]

survived_count=len(survived_passengers)

rate=(survived_count/len(data))*100

# print(rate)


male_passengers=[p for p in data if p.get("Sex")=="male"]

male_survived=[p for p in male_passengers if p.get("Survived")=="1"]

male_survived_rate=(len(male_survived)/len(male_passengers))*100

# print("male survival rate : ",male_survived_rate)


female_passengers=[p for p in data if p.get("Sex")=="female"]

female_survived=[p for p in female_passengers if p.get("Survived")=="1"]

female_survived_rate=(len(female_survived)/len(female_passengers))*100

# print("female survived rate : ",female_survived_rate)


total_class=[p.get("Pclass")for p in data]

passengers_count_class={p:total_class.count(p)for p in total_class}

print(passengers_count_class)

total_survived=[p.get("Pclass") for p in data if p.get("Survived")=="1"]

survived_passenger_class={s:total_survived.count(s)for s in total_survived}

print(survived_passenger_class)

for k,v in passengers_count_class.items():

    s_p=survived_passenger_class.get(k)

    rates=(s_p/v)*100
    
    print(k,rates)
    









