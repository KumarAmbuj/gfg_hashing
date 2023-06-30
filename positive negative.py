def findposneg(arr):

    dict={}

    for x in arr:

        if (0-x) in dict:
            print(0-x,' ',x)
            dict[0-x]=1
        else:
            dict[x]=1

arr = [ -4, 8, 9, 4, 1, -1, -8, -9 ]
findposneg(arr)
