lst=["10","20","hello","300","hai","4 00"]

number=[]

for n in lst:
    
    try:

       num=int(n)

       number.append(num)

    except Exception as e:

        continue

print(number)

max_element=max(number)
min_element=min(number)
sorted_element=sorted(number)
total=sum(number)

print(max_element)
print(min_element)
print(sorted_element)
print(total)





    