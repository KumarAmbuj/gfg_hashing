from collections import Counter
def groupwords(arr):

    dic=dict()

    for x in arr:

        worddict=Counter(x)

        k=worddict.keys()

        key=sorted(k)
        key=''.join(key)

        if key in dic:
            dic[key].append(x)
        else:
            dic[key]=[]
            dic[key].append(x)


    for x in dic:
        print(','.join(dic[x]))


input=['may','student','students','dog','studentssess','god','cat','act','tab','bat','flow','wolf','lambs','amy','yam','balms','looped','poodle']
groupwords(input)
