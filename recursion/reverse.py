def reverse(number):

    if number==0:

        return ""
    
    return str(number%10) +str(reverse(number//10))

print(reverse(543))

