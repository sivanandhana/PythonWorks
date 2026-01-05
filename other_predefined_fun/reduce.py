from functools import reduce

lst=[15,80,78,96,2,36]


max_num=reduce(lambda n1,n2 : n1 if n1>n2 else n2,lst)

# print(max_num)

min_num = reduce(lambda n1,n2 : n1 if n1<n2 else n2,lst)

# print(min_num)

product = reduce(lambda n1,n2 : n1*n2,lst)

print(product)