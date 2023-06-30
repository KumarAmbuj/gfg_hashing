def topk(arr,k):
    freq={i:0 for i in range(k+1)}

    top=[0 for i in range(k+1)]


    for x in arr:
        if x in freq:
            freq[x]+=1
        else:
            freq[x]=1

        top[k]=x

        i=top.index(x)
        i-=1

        while i>=0:


            if freq[top[i]]<freq[top[i+1]]:
                top[i],top[i+1]=top[i+1],top[i]

            elif freq[top[i]]==freq[top[i+1]] and top[i]>top[i+1]:
                top[i],top[i+1]=top[i+1],top[i]

            else:
                break

            i=i-1

        i=0
        while i<k and top[i]!=0:
            print(top[i],end=' ')
            i=i+1
k = 4
arr = [ 5, 2, 1, 3, 2 ]
n = len(arr)
topk(arr,  k)

