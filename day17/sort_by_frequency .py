l=[1,2,3,1,2,3,4,1,2,2,4,5,6,5,1,3,4]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
ans=""
for i in range(0,len(d)):
    m=0
    for key in d:
        if str(key) not in ans:
            if(d[key]>m):
                m=d[key]
                k=key

    ans+=str(k)*m
print(ans)
