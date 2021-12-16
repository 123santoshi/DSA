l=[1,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0]
s=""
for i in l:
    s+=str(i)
print(s)
l2=[]
s1=s.split("0")
l2.append(s1)
print(s1)
m=0
for i in s1:
    l3=len(i)
    if(l3>m):
        m=l3
print(m)
    
