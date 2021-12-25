n=int(input("enter number=="))
binary=bin(n)
binary=binary[2:]
print("binary representation of given number is==",binary)
rev_binary=list(reversed(binary))
ans=""
for i in rev_binary:
    ans+=i
print("reverse binary representation of given number==",ans)
if(binary==ans):
    print("palindrome")
else:
    print("not palindrome")
