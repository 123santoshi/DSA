def sum_calculate(i):
    total=0
    while(i>0):
        r=i%10
        i=i//10
        total+=r
    return total
l=[10,29,37,589,28,109,536,567,274]
sum_list=[]
for i in l:
    total=0
    while(i>0):
        r=i%10
        i=i//10
        total+=r
    sum_list.append(total)
print(sum_list)
print("list after sorting based on sum of digits==",sorted(sum_list))
sum_list=sorted(sum_list)
ans=[]
for i in sum_list:
    for j in range(0,len(l)):
        cal=sum_calculate(l[j])
        if(i==cal):
            if l[j] not in ans:
                ans.append(l[j])
                break
print("list after sorting based on sum of digits in original list",ans)
