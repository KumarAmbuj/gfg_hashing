def productpair(arr):
    s=set()

    for x in arr:
        s.add(x)

    result=0

    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):

            if arr[i]*arr[j] in s:
                result+=1

    return result

arr = [6, 2, 4, 12, 5, 3]
print(productpair(arr))
