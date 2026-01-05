def product_of_digit(number):

    if number==0:

        return 1
    
    return number%10*product_of_digit(number//10)

print(product_of_digit(46))