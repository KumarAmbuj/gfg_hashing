def findpairs(arr):
    s=set()
    for x in arr:
        s.add(x)

    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] in s:
                print(arr[i],' ',arr[j])
arr = [2, 8, 7, 1, 5]

findpairs(arr)