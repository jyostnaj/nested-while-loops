i=1
k=65
while i<=5:
    j=5
    c=65
    while j>=i:
        print(" ",end=" ")
        j-=1
    l=1
    while l<=i:
        print(chr(k),end=" ")
        l+=1
        c+=1
    print()
    i+=1
    k+=1