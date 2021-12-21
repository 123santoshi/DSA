'''check every character in string(number,capital letter,small letter,spl character )print it'''
s="abcdedf2345679ASDFGHJ#$%"
for i in s:
    asci=ord(i)
    if(asci>=49 and asci<=57):
        print(i,"is number")
    elif(asci>=65 and asci<=90):
        print(i,"is capital letter")
    elif(asci>=97 and asci<=122):
        print(i,"is small letter")
    else:
        print(i,"it is spl symbol")
