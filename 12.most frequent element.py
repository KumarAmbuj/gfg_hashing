def mostfrquent(arr):
    dict={}

    for x in arr:
        if x in dict:
            dict[x]+=1
        else:
            dict[x]=1

    mx=0
    ele=0

    for x in dict:
        if dict[x]>mx:
            mx=dict[x]
            ele=x

    print(ele)

