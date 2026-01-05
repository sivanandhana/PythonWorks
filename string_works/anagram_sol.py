def is_anagram(word1,word2):
    is_anagram_word=True
    if len(word1)!=len(word2):
        return False
    for ch in word1:
        ch_count_w1=word1.count(ch)

        ch_count_w2=word2.count(ch)

        if ch_count_w1!=ch_count_w2:

            is_anagram_word=False
            break
    return is_anagram_word
print(is_anagram("cat","act"))
print(is_anagram("nasa","sana"))
print(is_anagram("dog","gods"))