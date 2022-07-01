i=5
while i>=1:
    j=1
    while j<=5:
        if i==j or i==5 or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print()
    i-=1