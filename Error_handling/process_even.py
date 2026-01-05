file_path="Error_handling\\number.txt"

fr=open(file_path,"r",encoding="utf-8")

all_numbers=[]

for line in fr:
    line=line.rstrip("\n")
    try:
        num=int(line)
        all_numbers.append(num)
    except Exception as e:
        continue
    
print(all_numbers)

even_number=[]

for num in all_numbers:

    if num%2==0:
        even_number.append(num)

print(even_number)

even_count={num:even_number.count(num) for num in even_number}

print(even_count)

max_value=max(even_count.values())

frequent={k for k,v in even_count.items() if v==max_value}

print(frequent)









