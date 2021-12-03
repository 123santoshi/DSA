s=input("enter string=")
l=list(s)
i=0
j=len(l)-1
while(i<j):
    if(l[i].isalpha() and l[j].isalpha()):
        temp=l[i]
        l[i]=l[j]
        l[j]=temp
        i=i+1
        j=j-1
    elif(l[i].isalpha() and not(l[j].isalpha())):
        j=j-1
    else:
        i=i+1
ans=""
for i in l:
    ans+=i
print(ans)