#fiind out index of first unique chaarcter in string
s=input("enter string==")
d={}
for i in s:
    if i not in d.keys():
        d[i]=0
    d[i]=d[i]+1
print(d)
u=-1
for key in d:
    if(d[key]==1):
        u=key
        break
u=str(u)
if(u=='-1'):
    ans=-1
else:
    ans=s.index(u)
print(ans)