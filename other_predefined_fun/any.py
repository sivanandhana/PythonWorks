lst = ["program","problem","perfect","apple"]

# bool_list = [w.startswith("pro") for w in lst]

word = list(map(lambda w:w.startswith("pro"),lst))

print(any(word))

# print(any(bool_list))


number= 15


print (not any([number%i==0 for i in range(2,number)]))