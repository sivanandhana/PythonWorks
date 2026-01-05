def is_prime(num):
    flag=True
    for i in range(2,num):
        if num%i==0:
            flag=False
            break
    return flag
print(is_prime(5))
print(is_prime(9))