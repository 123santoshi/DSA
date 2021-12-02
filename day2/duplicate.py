l=[3,1,3,4,2]
d={}
for i in l:
    if i not in d.keys():
        d[i]=0
    d[i]=d[i]+1
for key in d:
    if(d[key]!=1):
        print(key)
