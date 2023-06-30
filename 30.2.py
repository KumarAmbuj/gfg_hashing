def removemin(arr1,arr2):
    dict={}
    count=0

    for x in arr1:
        if x in dict:
            dict[x]+=1
        else:
            dict[x]=1

    for x in arr2:
        if x in dict:
            dict[x]+=1
        else:
            dict[x]=1

    for x in dict:
        if dict[x]>1:
            count+=1

    return count

a = [ 1, 2, 3, 4 ]
b = [2, 3, 4, 5, 8 ]
n = len(a)
m = len(b)
print(removemin(a, b))