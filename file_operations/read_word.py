file_path="C:\\Users\\HP\\Desktop\\development-journey-py-sivanandhana\\python-works\\file_operations\\words.txt"

fr=open(file_path,"r")
result=[]

for line in fr:
    line=line.rstrip("\n")
    word=line.replace(" ","")
    result.append(word)
print(result)
