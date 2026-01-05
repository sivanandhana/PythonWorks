i=1
while(i<=20):
    if(i%3==0):
        print("fizz divisible by 3")
    elif(i%5==0):
        print("Buzz divisible by 5")
    elif(i%3==0 and i%5==0):
        print("fizzBuzz divisible by both")
    else:
        print(i)
    i+=1