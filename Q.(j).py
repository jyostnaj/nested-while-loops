a=int(input("enter number"))
i=0
while i<5:
    f=5-i
    while f>0:
        print(" ",end=" ")
        f-=1
    j=i+1
    while j>0:
        print(j,end=" ")
        j-=1
    print()
    i+=1