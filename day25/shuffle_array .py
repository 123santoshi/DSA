#shuffle array according to pos array
a=[1,2,3,4,5]
pos=[3,2,4,1,0]
l=a.copy()
for i in range(len(a)):
    l[pos[i]]=a[i]
print(l)
