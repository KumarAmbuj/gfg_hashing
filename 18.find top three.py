def topthree(arr):
    dict={}

    for x in arr:
        if x in dict:
            dict[x]+=1
        else:
            dict[x]=1

    first=0

    sec=0
    thi=0

    firste=0
    sece=0
    thie=0

    for x in dict:
        if dict[x]>first:
            thi=sec
            thie=sece
            sec=first
            sece=firste

            first=dict[x]
            firste=x

        elif dict[x]>sec:
            thi=sec
            thie=sece

            sec=dict[x]
            sece=x

        elif dict[x]>thi:
            thi=dict[x]
            thie=x

    print(firste,sece,thie)

arr = [3, 4, 2, 3, 16, 3, 15, 16, 15, 15, 16, 2, 3]

topthree(arr)
