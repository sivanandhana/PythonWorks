num1=int(input("enter number 1 = "))
num2=int(input("enter number 2 = "))

try:
    result=num1/num2
    print(result)

except Exception as e:
    num2=int(input("Enter a number = "))
    result=num1/num2
    print(result)
    
finally:
    print("sending text message.....")
    print("sending email.....")
