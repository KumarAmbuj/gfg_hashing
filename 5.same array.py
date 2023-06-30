def samearray(arr):
    dict={}

    for x in arr:
        if x not in dict:
            dict[x]=1
        else:
            dict[x]+=1
    mx=0

    for x in dict:
        mx=max(mx,dict[x])

    return len(arr)-mx
arr = [4, 3, 4, 4, 2, 4]
print(samearray(arr))