nums=[1,4,2,5,6,1]
n=len(nums)
l=[-1]*n
for i in range(n):
    c=0
    for j in range(i,n):
        if(nums[i]<nums[j]):
            l[i]=nums[j]
            c=1
            break
print(l)
