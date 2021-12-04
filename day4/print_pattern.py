'''print the pattern 1,1,2,3,4,9,8,27,16,81,32,243,64,729...
    and print the nth elemnt in the series'''
num=int(input("enter how many elements u want=="))
n=int(input("enter nth element =="))
l=[]
even=1
odd=1
for i in range(0,num):
    if(i%2==0):
        if(i==0):
            even=1
            l.append(even)
        else:
            even=even*2
            l.append(even)
    else:
        if(i==1):
            odd=1
            l.append(odd)
        else:
            odd=odd*3
            l.append(odd)
print("the series ==",l)
print("nth element in the given series==",l[n-1])
        
