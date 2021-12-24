'''add plus one to the last digit of array if it is less than 9
2)if last digit is 9 then put zero and move to the left until we get number
ex:=[1,2,3,4]=last digit is equal to 4 so add +1 we get [1,2,3,5]
ex:=[1,2,3,9]=last digit is 9 so replace 9 with zero and move to left=[1,2,4,0
ex:=[9,9,9]=[1,0,0,0]
'''
def fun(l,index):
    while(index>=0):
        if(l[index]==9):
            l[index]=0
        else:
            l[index]=l[index]+1
            return l
        index=index-1
    l.insert(0,1)
    return l
        
l=[9,9,9]
index=len(l)-1
ans=fun(l,index)
print("ans==",ans)
