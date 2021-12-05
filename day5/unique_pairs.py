'''identify unique pairs  such that each of the integers in the pair have the same sum of the digits'''
l=[334,89,6,321,53,45,2211,81]
d={}
for i in l:
    temp=i
    s=0
    while(i>0):
        r=i%10
        s=s+r
        i=i//10
    if temp not in d:
        d[temp]=s
pairs=[]
for key in d:
    m=d[key]
    for keys in d:
        if(key==keys):
            continue
        else:
            if(d[keys]==m):
                pairs.append((key,keys))
#print(pairs)
ans=len(pairs)//2
if(ans==0):
    print("total number of unique pairs are==",-1)
else:
    print("total number of unique pairs are==",ans)






    