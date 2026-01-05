for r in range(1,6):
    for s in range(5,r-1,-1):
        print(" ",end="\t")
    for c in range(1,r+1):
        print("*",end="\t")
    print()
    
