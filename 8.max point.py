def maxpoint(arr):
    dict={}



    for i in range(1,len(arr)):
        x=arr[i-1]
        y=arr[i]

        if y[0]==x[0]:
           m='inf'
        else:
           m = (y[1] - x[1]) / (y[0] - x[0])

        if m in dict:
           dict[m] += 1
        else:
           dict[m] = 2

    mx=0
    for x in dict:
        mx=max(mx,dict[x])

    print(mx)

points = [(-1, 1), (0, 0), (1, 1), (2, 2), (3, 3), (3, 4)]

maxpoint(points)