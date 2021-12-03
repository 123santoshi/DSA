s=input("enter string==")
l=""
for i in s:
    if i not in l:
        l=l+i
l=l[::-1]
print("reverse the given string after removing duplicates ==",l)