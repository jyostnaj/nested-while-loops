a=int(input("enter number"))
i=a
while i>=1:
    f=a
    while f>=i:
        print(f,end=" ")
        f-=1
    print()
    i-=1