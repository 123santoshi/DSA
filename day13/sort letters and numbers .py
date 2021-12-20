'''sort letters in ascending order and then sort numbers in ascending order'''
s="B4A1D34rtsavcd"
char=""
num=""
for i in s:
    if i.isalpha():
        char+=i
    else:
        num+=i
final_ans=""
char=sorted(char)
num=sorted(num)
for i in char:
    final_ans+=i
for i in num:
    final_ans+=i
print(final_ans)
