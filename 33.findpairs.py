def findpairs(arr,sum):
    dic=dict()
    count=0

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            dic[arr[i][j]]=i

    print(dic)

    list=[]
    for i in range(len(arr)):


        for j in range(len(arr[0])):
            l = []

            if (sum-arr[i][j] in dic) and (dic[sum-arr[i][j]]!=i):
                l.append(arr[i][j])
                l.append(sum-arr[i][j])
                list.append(l)




    for x in list:
        print(x,end=' ')

n = 4
sum = 11
mat = [[1, 3, 2, 4],
        [5, 8, 7, 6],
        [9, 10, 13, 11],
        [12, 0, 14, 15]]
findpairs(mat, sum)




