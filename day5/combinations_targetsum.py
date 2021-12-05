'''set of numbers given ans sum is given
print the number of combinations possible of length 4 which sum is equal to the given sum'''
import itertools as it
l=[-1,1,0,0,2,-2]
length=4
target=0
c=list(it.combinations(l,4))
#print(c)
l2=[]
for i in c:
    if(sum(i)==target):
        l2.append(i)
print(l2)