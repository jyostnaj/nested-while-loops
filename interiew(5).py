n=int(input("enter number"))
i=1
while i<=n:
    j=n
    while j>i:
        print(" ",end="")
        j-=1
    l=1
    while l<=i:
        if i==1 or i==5 or l==1 or l==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        l+=1
    print()
    i+=2