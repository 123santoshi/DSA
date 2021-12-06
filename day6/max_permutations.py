'''find the permutations of given string and print maximum number in the permutations'''
import itertools
s="123"
l=len(s)
per=list(itertools.permutations(s,l))
l2=[]
for i in per:
    ans=""
    for j in i:
        ans+=str(j)
    l2.append(ans)
print("possible permutations are==",l2)
maximum=0
for i in l2:
    if(int(i)>maximum):
        maximum=int(i)
print("maximum number in possible permutations==",maximum)
        
