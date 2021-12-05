'''given string contains special chaarcters,digits,alphabets..separate the digits from givne string  and count the no of spl characters
    1)if spl characters count is odd then append odd digits and even digits alternatively ,start with odd digit
    2)1)if spl characters count is even then append even  digits and odd digits alternatively ,start with even digit'''
s=input("enter string==")
even=[]
odd=[]
spl=0
for i in s:
    if(i.isdigit()):
        if(int(i)%2==0):
            even.append(i)
        else:
            odd.append(i)
    if not(i.isalnum()):
        spl=spl+1
length=max(len(even),len(odd))
ans=""
if(spl%2==0):
    for i in range(0,length):
        if(i<len(even)):
            ans+=even[i]
        if(i<len(odd)):
            ans+=odd[i]
else:
    for i in range(0,length):
        if(i<len(odd)):
            ans+=odd[i]
        if(i<len(even)):
            ans+=even[i]
print(ans)
    
            
    