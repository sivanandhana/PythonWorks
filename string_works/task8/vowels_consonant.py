def vowels_consonant_count(word):
    v_count=0
    c_count=0
    vowels="aeiou"
    for ch in word.casefold():
        if ch in vowels and ch.isalpha():
            v_count+=1
        else:
            c_count+=1
    print("vowels count",v_count)
    print("consonant count",c_count)
vowels_consonant_count("hello world")
