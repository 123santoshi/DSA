#seperate even and odd index characters 
s="ancdefghij"
even=""
odd=""
for i in range(0,len(s)):
    if(i%2==0):
        even+=s[i]
    else:
        odd+=s[i]
print("even place string values==",even)
print("odd place string values==",odd)
