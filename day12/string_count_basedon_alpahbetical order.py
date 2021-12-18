#a=1,b=2,c=3.....z=26
s=input("enter string==")
total=0
for i in s:
    print("ASCII CODE OF",i, "==",ord(i))
    total+=ord(i)-96
print("sum of total string characters ==",total)
