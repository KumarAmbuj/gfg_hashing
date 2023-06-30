def nonovrsum(arr1,arr2):

    dict={}

    for x in arr1:
        dict[x]=1

    for x in arr2:
        if x in dict:
            dict[x]+=1

        else:
            dict[x]=1

    sum=0
    for x in dict:

        if dict[x]==1:
            sum+=x

    print(sum)

A = [1, 5, 3, 8]
B = [5, 4, 6, 7]
nonovrsum(A,B)


