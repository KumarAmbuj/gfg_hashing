def quadruples(arr1,arr2,arr3,arr4,sum):
    dic=dict()

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]+arr2[j] in dic:
                dic[arr1[i]+arr2[j]]+=1
            else:
                dic[arr1[i] + arr2[j]] =1



    count=0
    for i in range(len(arr3)):
        for j in range(len(arr4)):
            if (x-(arr3[i]+arr4[j])) in dic:
                count+=dic[x-(arr3[i]+arr4[j])]

    return count

arr1 = [1, 4, 5, 6]
arr2 = [2, 3, 7, 8]
arr3 = [1, 4, 6, 10]
arr4 = [2, 4, 7, 8 ]
n = len(arr1)
x = 30
print(quadruples(arr1,arr2,arr3,arr4,x))
