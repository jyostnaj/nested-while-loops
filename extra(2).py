name=input("enter name")
a=("a","e","i","o","u")
i=0
while i<len(name):
    if name[i] in a:
        print(name[i])
    i+=1
b=0
while i<len(name):
    if name[i] not in a:
        print(name[i])
    b+=1