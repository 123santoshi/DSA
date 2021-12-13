a=[1,3,4,2,1,3,4,4]
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
l=[]
for key in d:
    if(d[key]%2!=0):
        l.append(key)
print(l)