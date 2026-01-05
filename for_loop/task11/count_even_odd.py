num=int(input("enter a number : "))
count_even=0
count_odd=0
for i in range(1,num+1):
    if(i%2==0):
        count_even+=1
    else:
        count_odd+=1
print("count of even numbers : ",count_even)
print("count of odd numbers : ",count_odd)