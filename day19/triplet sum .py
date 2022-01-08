'''TRIPLET SUM IN ARRAY which is equal to X'''
def find3Numbers(A, n, X):
        # Your Code Here
    A=sorted(A)
    for i in range(n):
        low=i+1
        high=n-1
        r=X-A[i]
        while(low<high):
            s=A[low]+A[high]
            if(r==s):
                return 1
            elif(r<s):
                high-=1
            else:
                low+=1
        return 0
n=6
X=13
arr=[1,4,45,6,10,8]
ans=find3Numbers(arr,n,X)
print(ans)
