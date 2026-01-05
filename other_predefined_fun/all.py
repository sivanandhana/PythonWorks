# lst = [10,12,4,18,24,25,19]

lst = [10,12,4,18,24]

even=list(map(lambda n:n%2==0,lst))

is_all_b_num = all(even)

# print(is_all_b_num)



lst=["housefull","beautiful","peaceful","harmful","thinkful","powerful"]

word = list(map(lambda w:w.endswith("ful"),lst))

# bool_list = [w.endswith("full") for w in lst]  


print(all(word))


