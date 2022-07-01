row=1
while row<=5:
    col=1
    while col<=5:
        if col==1 or col==5 or col==row:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    print()
    row+=1