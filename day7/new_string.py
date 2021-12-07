'''write program to get a string of the first 2 characters and the last 2 characters from a given string,if the given string length is less than 2 return -1'''
s=input("enter string==")
if(len(s)>2):
    a=s[0:2]
    a2=s[-2:]
    ans=a+a2
    print(ans)
if(len(s)<=2):
    ans=s+s
    print(ans)
if(len(s)<2):
    ans="-1"
    print(ans)