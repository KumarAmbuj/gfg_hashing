def cumulative(arr):
    dic=dict()

    for x in arr:
        if x not in dic:
            dic[x]=1
        else:
            dic[x]+=1


    res=0

    for x in dic:
        res=res+dic[x]
        dic[x]=res

    for x in dic:
        print(x,'->',dic[x])


a = [1, 3, 2, 4, 2, 1]
n = len(a)
cumulative(a)
