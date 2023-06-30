def smallestsubarray(arr):
    left={}
    count={}

    mx=0
    mn=0
    startindex=-1


    for i in range(len(arr)):
        if arr[i] not in count:
            left[arr[i]]=i
            count[arr[i]]=1

        else:
            count[arr[i]]+=1



        if count[arr[i]]>mx:
            mx=count[arr[i]]
            mn=i-left[arr[i]]+1
            startindex=left[arr[i]]

        elif count==count[arr[i]] and ((i-left[arr[i]]+1)<mn):
            mx=count[arr[i]]
            mn=i-left[arr[i]]+1
            startindex=left[arr[i]]

    for i in range(startindex,startindex+mn):
        print(arr[i],end=' ')

arr = [4, 1, 1, 2, 2, 1, 3, 3]
smallestsubarray(arr)

