s="3[a]2[bc]"
stack=[]
for i in s:
    if(i!=']'):
        stack.append(i)
    else:
        sub=""
        while(stack[-1]!='['):
            sub+=stack.pop()
        stack.pop()
        n=""
        while(stack[-1].isdigit()and stack):
            n+=stack.pop()
            stack.append(int(n)*sub)
print("".join(stack))
