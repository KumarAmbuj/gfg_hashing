def countpairs(arr,sum):
    dic=dict()

    for i in range(len(arr)):
        if arr[i] in  dic:
            dic[arr[i]]+=1
        else:
            dic[arr[i]]=1

    count=0

    for x in arr:

        if sum-x in dic:

            count+=dic[sum-x]
        if sum-x==x:
            count-=1

    return count//2

arr = [1, 5, 7, -1, 5] 
n = len(arr)
sum = 6

print(countpairs(arr,sum))





