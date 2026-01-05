file_path="file_operations\\task26_11\\name.txt"

fr=open(file_path,"r")

for line in fr:

    line=line.rstrip("\n")

    first_name=line[0]

    last_name=line[-1]

    print(first_name,last_name)

   
  

