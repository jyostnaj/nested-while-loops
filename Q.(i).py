a=int(input("enter number"))
i=1
while i<=5:
    f=1
    while f<=5-i:
        print(" ",end=" ")
        f+=1
    j=1
    while j<=i:
        print(i,end=" ")
        j+=1
    print()
    i+=1