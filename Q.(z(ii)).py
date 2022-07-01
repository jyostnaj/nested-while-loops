a=int(input("enter number"))
i=5
while i>=1:
    f=1
    while f<=5-i:
        print(" ",end=" ")
        f+=1
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i-=1