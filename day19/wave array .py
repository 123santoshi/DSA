def convertToWave(arr):
    for i in range(0,len(arr)-1,2):
        arr[i],arr[i+1]=arr[i+1],arr[i]
    print(arr)
arr=[1,2,3,4,5]
convertToWave(arr)
