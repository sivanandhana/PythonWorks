def is_anagram(word1,word2):
    srt_w1 = sorted(word1)
    srt_w2 = sorted(word2)
    return srt_w1==srt_w2
print(is_anagram("listen","silent"))
print(is_anagram("wello","hello"))
print(is_anagram("god","dog"))