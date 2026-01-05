def consonants(word):
    count=0
    VOWELS="aeiou"
    for ch in word.casefold():
        if ch not in VOWELS and ch.isalpha():
            count+=1
   
    return count
print(consonants("hello23"))
print(consonants("hai"))