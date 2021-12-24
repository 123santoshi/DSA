'''add all characters to 1 string and add all numbers to another string'''
s=" 2018 india is my country 18"
alpha=""
num=0
s=s.split()
for i in s:
    if(i.isdigit()):
        num+=int(i)
    else:
        alpha+=i
        print("\t")
print("words==",alpha)
print("numbers sum==",num)
