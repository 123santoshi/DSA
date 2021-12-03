'''input= A string of comma sepaarted numbers are given such that numbers 4 and 7 already present in the list.Assume that 7 always comes after 4 in the given string
cases:-
num1=add all numbers which do not lie betweeen 4 and 7 excluding(4 and 7)
num2=numbers formed by concatenating all numbers from 4 to 7 including(4 and 7)'''
l=[3,1,6,4,2,3,7,2]
f=l.index(4)
s=l.index(7)+1
s2=l[f:s]
l2=[]
#sum the numbers which is not in range of 4,7
num1=0
for i in range(0,len(l)):
    if i not in range(f,s):
        num1=num1+l[i]
num2=""
for i in range(0,len(l)):
    if i in range(f,s):
        num2=num2+str(l[i])
total=num1+int(num2)
print("sum of num1 and num2 is==",total)






    
    

    
    
