file_path="file_operations\\task26_11\\numbers.txt"

fr=open(file_path,"r")

for line in fr:
    num=int(line.rstrip("\n"))
    digit=num%10
    print(digit)
    