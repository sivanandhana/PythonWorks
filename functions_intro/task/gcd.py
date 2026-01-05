def gcd(n1,n2):
    small=min(n1,n2)
    result=1
    for i in range(1,small+1):
        if n1%i==0 and n2%i==0:
            result=i
    return result
print(gcd(12,18))
print(gcd(10,5))
print(gcd(4,6))