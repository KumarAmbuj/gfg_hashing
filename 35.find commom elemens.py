def findcommon(arr):
    dic=dict()

    for i in range(len(arr)):
        dic[arr[0][i]]=1

    for i in range(1,len(arr)):
        temp=dict()

        for j in range(len(arr)):

            temp[arr[i][j]]=1

        for itr in list(dic):
            if itr not in temp:
                del dic[itr]

        if len(dic)==0:
            break

    for itr in dic:
        print(itr)
mat = [[2, 1, 4, 3],
       [1, 2, 3, 2],
       [3, 6, 2, 3],
       [5, 2, 5, 3]]
findcommon(mat)