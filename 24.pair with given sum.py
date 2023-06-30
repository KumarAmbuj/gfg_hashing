def pairsum(arr,sum):
    dict={}
    mn=0
    n=len(arr)

    for i in range(len(arr)):
        if sum-arr[i] not in dict:
            dict[arr[i]]=min(i+1,n-i)

        else:
            dict[arr[i]]=min(i+1,n-i)
            mn=max(dict[arr[i]],dict[sum-arr[i]])

    print(mn)

a = [2, 4, 1, 9, 5]

pairsum(a,3)