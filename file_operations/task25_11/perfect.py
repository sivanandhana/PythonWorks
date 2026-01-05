

file_path="file_operations\\task26_11\\numbers.txt"

fr_perfect=open(file_path,"r")


for line in fr_perfect:

    
    sum=0

    num=int(line.rstrip("\n"))

    for i  in range(1,num):

        if num%i==0:

            sum+=i

    if sum==num:
        print(num)

    
           
        
