l=[]
n=int(input("enter no of elements=="))
for i in range(0,n):
    val=int(input("enter value=="))
    l.append(val)
print("the entered list is==",l)
s=[]
for i in l:
    if i not in s:
        s.append(i)
print(s)
s=s[::-1]
print(s)