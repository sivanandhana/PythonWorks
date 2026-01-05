file_path="C:\\Users\\HP\\Desktop\\development-journey-py-sivanandhana\\python-works\\file_operations\\numbers.txt"

fr=open(file_path,"r")

reverse=[]

for line in fr:

    number=(line.rstrip("\n"))

    rev= number[::-1]

    reverse.append(rev)

print(reverse)


        
    