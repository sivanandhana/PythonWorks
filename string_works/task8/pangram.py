def is_pangram_text(text):
    ALPHABET="abcdefghijklmnopqrstuvwxyz"
    is_pangram=True
    for al in ALPHABET:
        if al not in text:
            is_pangram=False
            break
    return is_pangram
print(is_pangram_text("hello world"))
print(is_pangram_text("abcdefghijklmnopqrstuvwxyz"))