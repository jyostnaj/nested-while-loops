n=int(input("enter number"))
i=1
while i<=n:
    j=n
    while j>=i:
        print(" ",end="")
        j-=1
    l=1
    while l<=i:
        print("*",end=" ")
        l+=1
    print()
    i+=1