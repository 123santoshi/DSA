#count no of squares 
r,c,s=4,3,1    #r-rows,c-columns
while(r!=1 and c!=1):
    s=s+r*c
    r-=1
    c-=1
print(s)
