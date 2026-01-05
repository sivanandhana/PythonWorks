def count_digit(n):

    if n==0:
        return 0
    
    return 1+ count_digit(n//10)

print(count_digit(235))