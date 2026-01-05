def sum_of_digits(number):

    if number==0:

        return 0
    
    return number%10+sum_of_digits(number//10)

print(sum_of_digits(54))

print(sum_of_digits(154))