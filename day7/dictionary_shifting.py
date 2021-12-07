'''take a string and separate key value pairs and find out the sum of  squares of digits in values..if sum is even then last two characters will be shifted to left ,if sum is odd first character will be placed last '''
d="abcd:1234,bcdgfhf:127836,sdjks:1245"
d=d.split(",")
for i in d:
    k,v=i.split(":")
    total=0
    for i in v:
        length=len(k)
        i=int(i)
        while(i>0):
            r=i%10
            total=r*r+total
            i=i//10
    if(total%2==0):
        ans=k[length-2:length]
        ans1=k[0:length-2]
        final_ans=ans+ans1
        print("final string after shifting dictionary is==",final_ans)
    else:
        ans=k[0]
        ans1=k[1:length]
        final_ans=ans1+ans
        print("final string after shifting dictionary is==",final_ans)
    