s=input("enter string==")
s2=input("enter string==")
s=set(s)
s2=set(s2)
ans=s.intersection(s2)
ans=sorted(ans)
final_string=""
for i in ans:
    final_string+=i
print("common elements in both strings are==",final_string)
