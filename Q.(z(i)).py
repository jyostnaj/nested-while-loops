a=int(input("enter number"))
i=1
while i<=a:
    f=a
    while f>i:
        print(" ",end="")
        f-=1
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i+=2
i=2
while i<a:
    f=1
    while f<=i:
        print(" ",end="")
        f+=1
    j=a
    while j>i:
        print("*",end=" ")
        j-=1
    print()
    i+=2