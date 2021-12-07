'''finding kth smallest elemnt in arr'''
l=[1,4,7,2,9,14,12]
k=int(input("enter kth element=="))
l=sorted(l)
print(l)
print("kth smallest number is==",l[k-1])