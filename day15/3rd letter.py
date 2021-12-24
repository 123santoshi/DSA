'''add 3 for every character ascii value'''
s="as3gAsd"
ans=""
for i in s:
    asci=ord(i)+3
    ans=ans+chr(asci)
print(ans)
