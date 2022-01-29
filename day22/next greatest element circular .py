nums=[1,4,2,5]
n=len(nums)
l=[-1]*n
for i in range(n):
    c=0
    for j in range(i,n):
        if(nums[i]<nums[j]):
            l[i]=nums[j]
            c=1
            break
        if(c==0):
            for k in range(0,i):
                if(nums[i]<nums[k]):
                    l[i]=nums[k]
                    c=1
                    break
print(l)
