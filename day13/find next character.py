'''a+4==e (4th element from a=e)
    k+3=n  (3rd element from k=n)
    b+2=d (2nd element from b=d)
'''
s="a4k3b2c5"
ans=""
if(len(s)%2==0):
    for i in range(0,len(s)):
        if s[i].isalpha():
            ans+=s[i]
        else:
            prev=ord(s[i-1])
            convert=int(s[i])
            add=chr(prev+convert)
            ans+=add
    print(ans)
