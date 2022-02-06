a="lrll"
ans="n"
for i in a:
    if i=="l" and ans=="n":
        ans="w"
    elif i=="l" and ans=="w":
        ans="s"
    elif i=="l" and ans=="s":
        ans="e"
    elif i=="l" and ans=="e":
        ans="n"
    elif i=="r" and ans=="n":
        ans="e"
    elif i=="r" and ans=="w":
        ans="n"
    elif i=="r" and ans=="s":
        ans="w"
    elif i=="r" and ans=="e":
        ans="s"
print(ans)
