def is_palindrome(word):
    word=word.casefold()
    return word==word[::-1]
print(is_palindrome("malayalam"))
print(is_palindrome("english"))
print(is_palindrome("Radar"))