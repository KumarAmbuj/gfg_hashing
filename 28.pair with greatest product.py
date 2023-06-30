import math
def pairproduct(arr):
    dict={}
    n=len(arr)
    arr=sorted(arr)

    for x in arr:
        if x in dict:
            dict[x]+=1
        else:
            dict[x]=1

    for i in range(n-1,0,-1):

        j=0

        while(j<i and arr[j]<=math.sqrt(arr[i])):

            if arr[i]%arr[j]==0:
                result=arr[i]//arr[j]

                if result!=arr[j] and result in dict and dict[result]>0:
                    return arr[i]

                elif result == arr[j] and result in dict and dict[result]>1:
                    return arr[i]

            j+=1

    return -1

arr= [17, 2, 1, 15, 30]
n = len(arr)
print(pairproduct(arr))