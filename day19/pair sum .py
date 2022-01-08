def Countpair(arr,n,x) : 
    c=0
    i=0
    j=n-1
    while(i<j):
        s=arr[i]+arr[j]
        if(s==x):
            c+=1
            i+=1
            j-=1
        elif(s<x):
            i+=1
        else:
            j-=1
    if(c>0):
        return c
    else:
        return -1

n=7
arr=[1,2,3,4,5,6,7]
X=8
ans=Countpair(arr,n,X)
print("no of pairs are",ans)
