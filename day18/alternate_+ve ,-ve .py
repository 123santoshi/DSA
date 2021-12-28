arr=[9,4,-2,-1,5,0,-5,-3,2]
p=[]
n=[]
for i in arr:
    if(i>=0):
        p.append(i)
    else:
        n.append(i)
l3=[]
m=max(len(p),len(n))
for i in range(0,m):
    if(i<len(p)):
        l3.append(p[i])
    if(i<len(n)):
        l3.append(n[i])
arr=l3
print(arr)
