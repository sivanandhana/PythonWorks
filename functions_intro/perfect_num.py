def is_perfect_number(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return sum == num
print(is_perfect_number(6))