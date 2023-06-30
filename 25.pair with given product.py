def pairproduct(arr,k):
    s=set()

    for x in arr:
        if x ==0:
            if k==0:
                return True
            else:
                continue

        if k%x==0:

            if k//x in s:
                return True

            s.add(x)

    return False


arr = [10, 20, 9, 40]
x = 400
print(pairproduct(arr,x))
