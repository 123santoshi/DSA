s=input("enter sentence==")
l=s.split()
ans=""
for i in l:
    i=i[::-1]
    ans=ans+i+" "
print(ans)