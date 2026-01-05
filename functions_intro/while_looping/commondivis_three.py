num1=int(input("enter a number1 : "))
num2=int(input("enter a number2 : "))
num3=int(input("enter a number3 : "))
i=1
small=0
if(num1<num2 and num1<num3):
    small=num1
elif(num2<num1 and num2<num3):
    small=num2
else:
    small=num3
while(i<=small):
    if(num1%i==0 and num2%i==0 and num3%i==0):
        print(i)
    i+=1
