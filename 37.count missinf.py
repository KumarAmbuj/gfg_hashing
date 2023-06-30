def permutation(arr):
    dic=dict()
    n=len(arr)

    for x in arr:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    nextmissing=1

    for i in range(len(arr)):

        if dic[arr[i]]!=1 or arr[i]>n or arr[i]<1:
            dic[arr[i]]-=1


            while dic.get(nextmissing):
                nextmissing+=1

            arr[i]=nextmissing
            dic[nextmissing]=1

    for i in range(len(arr)):
        print(arr[i])
A = [ 2, 2, 3, 3 ]
n = len(A)
permutation(A)