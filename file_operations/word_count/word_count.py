word_path="file_operations\\word_count\\story.txt"

fr_word_count=open(word_path,"r")

wc={}

for line in fr_word_count:
    
    line=line.rstrip("\n")

    word=line.split(" ")

    for w in word:

        w=w.rstrip(",")

        w=w.rstrip(".")
        
        if w in wc:

            wc[w]+=1

        else:

            wc[w]=1

# print(wc)

max_wc=max(wc.values())

# print(max_wc)

for k,v in wc.items():

    if v==max_wc:

        print(k,v)

    











