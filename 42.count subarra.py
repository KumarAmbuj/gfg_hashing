def countsubarray(arr,k):
    dic=dict()



    count=0

    sum=0

    for x in arr:
        sum=sum+x

        if sum==k:
            count+=1

        if sum-k in dic:
            count+=dic[sum-k]

        if sum in dic:
            dic[sum]+=1
        else:
            dic[sum]=1

    return count

arr =  [10, 2, -2, -20, 10]
Sum = -10
n = len(arr)
print(countsubarray(arr,Sum))


