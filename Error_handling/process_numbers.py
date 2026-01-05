file_path="Error_handling\\numbers.txt"

try:

    fr=open(file_path,"r")

    list=[]

    for line in fr:

        line=line.rstrip("\n")

        try:
            num=int(line)
            list.append(num)
        except Exception as e:

            continue

    print(list)

    maximum_element=max(list)
    minimum_element=min(list)
    total=sum(list)

    print("maximum = ",maximum_element)
    print("minimum = ",minimum_element)
    print("sum = ",total)

    number_count={num:list.count(num) for num in list}

    max_value=max(number_count.values())

    frequency=[k for k,v in number_count.items() if v==max_value]
    
    print("frequency = ",frequency)

except Exception as e:

    print(e)




