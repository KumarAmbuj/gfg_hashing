def findkmissing(arr1,arr2,k):



    count=0

    for x in arr1:
        if x not in arr2:
            count+=1

            if count==k:
                return x
    return -1
a = [0, 2, 4, 6, 8, 10, 12, 14, 15]
b = [4, 10, 6, 8, 12]
print(findkmissing(a,b,3))