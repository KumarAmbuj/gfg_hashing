def givensum(arr,sum):
    s=set()

    for x in arr:
        if (sum-x) in s:
            print(x, " and", sum-x)
        else:
            s.add(x)

A = [1, 4, 45, 6, 10, 8]
givensum(A,16)