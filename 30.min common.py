def removemin(arr1,arr2):

    s=set()

    for x in arr1:
        s.add(x)

    count=0

    for x in arr2:
        if x in s:
            count+=1

    return count

a = [ 1, 2, 3, 4 ]
b = [2, 3, 4, 5, 8 ] 
n = len(a)
m = len(b)
print(removemin(a, b))