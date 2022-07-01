a=int(input("enter number"))
k=1
i=1
while i<=5:
    f=1
    while f<=5-i:
        print(" ",end=" ")
        f+=1
    j=1
    while j<=k:
        print(i,end=" ")
        j+=1
    k+=2
    print()
    i+=1