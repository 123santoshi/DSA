'''
input=input will be any number ,separate odd places integers ,you have to return 4 digit OTP by squaring the digits and print first 4 digits of your OTP
example:-
number=5624381275
odd place digits are=6,4,8,2,5
squaring those numbers are==36 16 64 4 25
first 4 digits of OTP are=3616'''
n=int(input("enter number=="))
n=str(n)
l=[]
for i in range(0,len(n)):
    if(i%2!=0):
        l.append(int(n[i]))
l=[i**2 for i in l]
ans=""
for i in l:
    ans=ans+str(i)
print(ans[:4])


        

        






    
    

    
    
