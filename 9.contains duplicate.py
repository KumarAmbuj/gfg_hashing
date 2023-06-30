def findduplicate(arr,k):
    dict={}

    for i in range(len(arr)):
        if arr[i] not in dict:
            dict[arr[i]]=i

        else:
            if i-dict[arr[i]]<=k:
                return True

    return False

arr = [10, 5, 3, 4, 3, 5, 6]
print(findduplicate(arr,3))