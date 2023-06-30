def minsubset(arr):
    dict={}

    for x in arr:
        if x in dict:
            dict[x]+=1
        else:
            dict[x]=1

    res=0
    for key, value in dict.items():
        res=max(res,value)


    print(res)


ar = [5, 6, 9, 3, 4, 3, 4]
n = len(ar)
minsubset(ar)
