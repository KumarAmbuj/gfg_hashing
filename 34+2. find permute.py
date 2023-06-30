def findpermute(arr,k):
    s=set()

    for i in range(len(arr)):
        s.add(arr[k][i])

    for i in range(len(arr)):
        if i==k:
            continue
        for j in range(len(arr)):

            if arr[i][j] not in s:
                break

        else:
            print(i,end=' ')


mat = [[3, 1, 4, 2],
       [1, 6, 9, 3],
       [1, 2, 3, 4],
       [4, 3, 2, 1]]
findpermute(mat,3)