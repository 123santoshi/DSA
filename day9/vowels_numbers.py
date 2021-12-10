s="Language"
#s=input("enter string==")
s=s[::-1]
print("reverse of the given string is==",s)
vowels="aeiouAEIOU"
count=0
for i in s:
    if i in vowels:
        count=count+1
ans=""
for i in s:
    if i in vowels:
        ans=ans+str(count)
        count=count-1
    else:
        ans=ans+i
print("after changing vowels with numbers=",ans)
        