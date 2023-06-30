def maxoccur(arr):
    dict={}
    mx=0
    for i in range(len(arr)):

        if arr[i] not in dict:
            dict[arr[i]]=i

        else:
            mx=max(mx,i-dict[arr[i]])

    print(mx)

arr=[3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
maxoccur(arr)