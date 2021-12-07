'''to get a string where all occurances of its first char have been changed to  "#" except first character'''
s=input("enter string==")
a=s[0]
ans=""
ans+=a
for i in range(1,len(s)):
    if(s[i]==a):
        ans+='#'
    else:
        ans+=s[i]
print(ans)