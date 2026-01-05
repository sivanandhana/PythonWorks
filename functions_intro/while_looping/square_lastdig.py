num=int(input("enter a number : "))
while(num!=0):
    last_digit=num%10
    square=last_digit**2
    print(square)
    num=num//10
