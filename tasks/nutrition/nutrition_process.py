file_path="nutrition\\Food_Nutrition_Dataset.csv"

fr=open(file_path,"r")

import csv

reader=csv.DictReader(fr)

data=[row for row in reader]


# print("number of food items=",len(data))


all_categories=[f.get("category") for f in data]

# print("all categories=",all_categories)


food_categories={c:all_categories.count(c) for c in all_categories}

# print("foods categories",food_categories)


maximum=max(food_categories.values())

minimum=min(food_categories.values())

# print(minimum)

# print(maximum)


protein=sorted(data,key=lambda f:f.get("protein"),reverse=True)
 
# print(protein)


first_six_food =protein[:6]

# print(first_six_food)

all_calorie_items={dic.get("food_name"):float(dic.get("calories",0)) for dic in data}

# print(all_calorie_items)

max_calories=max(all_calorie_items)

# print(max_calories)

Cakes_pies=[c for c in data if c .get("category")=="Cakes and pies"]

# print(Cakes_pies)


vitamin=[v.get("vitamin_c") for v in data]

# print(vitamin)

vitamin_int=[]

for v in vitamin:

    v==float(v)

    print(v)



# max_vitamim=max(vitamin)

# print(max_vitamim)

