'''to find the index of numerics and print it as a string'
input==012abgh52
output==
index of o=0
index of 1=1
index of 2=2
index pf 5 =7
index of 2=8
combine all values we get==01278'''
s="012abgh52"
ans=""
for i in range(0,len(s)):
    if(s[i].isdigit()):
        ans+=str(i)
print("indexes of numeric values==",ans)
