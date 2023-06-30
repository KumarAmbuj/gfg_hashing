def nonovrsum(arr1,arr2):
    s=set()

    sum=0
    for x in arr1:
        s.add(x)
        sum+=x

    for x in arr2:
        if x in s:
            sum=sum-x
        else:
            sum+=x
    print(sum)
A = [1, 5, 3, 8]
B = [5, 4, 6, 7]
nonovrsum(A,B)

