'''Find the maximum digit from code which is less than <= the length of name and put the place char in the finalstring if there is no any digit found which satisfy the given condition then print "X"
'''
s="Sonakshi:34848,Naman:4739,Prachi:2949,Ekta:9889"
l=s.split(",")
l2=[]
for i in l:
    k,v=i.split(":")
    length=len(k)
    maximum=0
    for i in v:
        if(int(i)<=length):
            if(int(i)>maximum):
                maximum=int(i)
    if(maximum==0):
        l2.append('X')
    else:
        l2.append(k[maximum-1])
ans=""
for i in l2:
    ans+=str(i)
print("final decoded ouput is==",ans)
        
                
               
    
    
    