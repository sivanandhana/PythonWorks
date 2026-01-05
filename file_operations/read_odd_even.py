file_path="C:\\Users\\HP\\Desktop\\development-journey-py-sivanandhana\\python-works\\file_operations\\numbers.txt"
odd=[]
even=[]
fr=open(file_path,"r")
for line in fr:
    number=int(line.rstrip("\n"))
    if number%2==0:
        even.append(number)
    else:
        odd.append(number)

        
print(even)

print(odd)


