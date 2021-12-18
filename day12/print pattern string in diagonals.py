#take a string with odd length characters and mid element will be common then print diagoanlly
#below program works perfectly on odd length string"
s="santu"
r=s[::-1]
for i in range(0,len(s)):
    for j in range(0,len(s)):
        if(i==j):
            print(s[i],end="\t")
        elif(j==len(r)-1-i):
            print(r[i],end="\t")
        else:
            print("*",end="\t")
    print("\n")
