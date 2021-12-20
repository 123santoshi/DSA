s="a4b5c6d5"
ans=""
if(len(s)%2==0):
    for i in s:
        if i.isalpha():
            store=i
        else:
            ans=ans+store*int(i)
            
    print("final string after expanding ==",ans)
else:
    print("given string is invalid string")
