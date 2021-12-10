s=input("enter string==")
#s="abedbcusnx"
queryno=input("enter no of queries==")
#queryno=2
ans=""
for i in range(0,queryno):
    query=input("enter query string==")
    index=s.find(query)
    print(index)
    ans=ans+s[index:len(s)]
    print(ans)
    