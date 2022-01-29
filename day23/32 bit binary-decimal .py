x=5       #given number
b=bin(x)
b=b[2:]        #binary representaton of n
z=[0]*(32-len(b))  #create 32 bit list
s=""                #convert binary number into str
for i in z:
    s=s+str(i)
bi=s+b         
rbi=bi[::-1]   #reverse of 32 bit binary number 
ans=int(rbi,2)   #converting 32 bit binary number into decimal
print(ans)
