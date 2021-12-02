l=[[1,2,3],[4,5,6],[7,1,1]]
maximum=0
for i in range(0,len(l)):
    c=sum(l[i])
    if(c>maximum):
        maximum=c
print("maximum_customer_wealth ==",maximum)