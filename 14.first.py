def firstelement(arr,k):
    dict={}

    for x in arr:
        if x not in dict:
            dict[x]=1
        else:
            dict[x]+=1

    for x in dict:
        if dict[x]==k:
            print(x)
            break

    else:
        print(-1)

arr = [1, 7, 4, 3, 4, 8, 7];
n = len(arr)
k = 2
firstelement(arr,k)

