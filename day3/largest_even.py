'''input=take a string as input separate all the integers ,then take each integer only once
    and from largest even number ,print largest even number if possible if it is not possible to print largest even number print -1'''
n=input("enter string==")
#to add numbers into nums
nums=""
for i in n:
    if(i.isdigit()):
       nums+=i
nums=list(nums)
#to get the unique digits
unique=[]
for i in nums:
    if i not in unique:
        unique.append(i)
#to form the largest number
ans=""
for i in range(0,len(unique)):
    m=max(unique)
    ans=ans+m
    unique.remove(m)
#check if largest number is even or not
if(int(ans)%2==0):
    print("largest possible even integer is==",ans)
else:
    print("not possible to print largest possible even integer==",-1)

    
        

        






    
    

    
    
