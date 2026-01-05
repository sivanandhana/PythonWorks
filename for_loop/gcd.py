num1= int(input("enter a number1 : ") )
num2= int(input("enter a number2 : ") )
num3= int(input("enter a number3 : ") )
smallest= min(num1,num2,num3)
gcd = 0
for i in range(1,smallest+1):
    if(num1%i==0 and num2%i==0 and num3%i==0):
        gcd=i
print(gcd)