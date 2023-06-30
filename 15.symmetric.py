def symmetric(arr):
    dict={}

    for i in range(len(arr)):
        first=arr[i][0]
        sec=arr[i][1]

        if sec not in dict:
            dict[first]=sec

        else:
            print("(",first,",",sec,")")

arr = [[11, 20], [30, 40], [5, 10], [40, 30],[10, 5]]

symmetric(arr)