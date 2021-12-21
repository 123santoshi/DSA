'''convert a -z,b-y,c-x,........z-a'''
s=input("enter string==")
ans=""
for i in s:
    add=122+97-ord(i)
    ans+=chr(add)
print("aafter changing the string will become===",ans)
