'''check if target number present in every subset r not if it is present in every subset then print 1 else print 0'''
length=int(input("enter length of list=="))
l=[]
for i in range(0,length):
    val=int(input("enter value=="))
    l.append(val)
print(l)
target=int(input("enter number we want to check=="))
subset=int(input("enter subset length=="))
l2=[]
for i in range(0,len(l),subset):
    l2.append(l[i:i+subset])
print(l2)
for i in l2:
    if target in i:
        a=1
    else:
        a=0
        break
if(a==1):
    print("1")
else:
    print("0")
