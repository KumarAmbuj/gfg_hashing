def unionandintersection(arr1,arr2):
    union=[]
    inter=[]

    dict={}

    for x in arr1:
        dict[x]=1

    for x in arr2:
        if x in dict:
            dict[x]+=1
        else:
            dict[x]=1

    for x in dict:
        union.append(x)

        if dict[x]>1:
            inter.append(x)

    print(union)
    print(inter)

arr1=[5 ,4, 3, 2, 1 ]
arr2=[6,5,3,1]

unionandintersection(arr1,arr2)