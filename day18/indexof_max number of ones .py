arr=[[0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]]
n=4
m=4
l=[]
for i in range(0,n):
    c=0
    for j in range(0,m):
        if(arr[i][j]==1):
            c=c+1
    l.append(c)
print(l)
m=max(l)
print(l.index(m))
