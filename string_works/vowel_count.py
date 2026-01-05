def vowel_count(word):
    count=0
    vowels="aeiou"
    for ch in word.casefold():
        if ch in vowels:
            count+=1
    return count
print(vowel_count("orange"))
print(vowel_count("APPLE"))