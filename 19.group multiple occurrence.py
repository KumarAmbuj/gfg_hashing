def group(arr):
    dict={}

    for x in arr:

        if x not in dict:
            dict[x]=1
        else:
            dict[x]+=1

    print(dict)

    for x in dict:
        print(str(x)*dict[x],end='')

arr = [4, 6, 9, 2, 3, 4, 9, 6, 10, 4]

group(arr)