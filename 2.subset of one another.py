def check(arr1,arr2):
    s=set(arr1)


    for x in arr2:

        if x not in s:
            return False

    return True

arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1,4]

print(check(arr1,arr2))