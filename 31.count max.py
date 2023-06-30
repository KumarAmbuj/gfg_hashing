def countcommon(arr1,arr2):
    dict={}
    for x in arr1:
        dict[x[0]]=x[1]

    count=0
    for x in arr2:
        if x[0] in dict and dict[x[0]]!=x[1]:
            count+=1

    print(count)


list1 = [("apple", 60), ("bread", 20),
         ("wheat", 50), ("oil", 30)]
list2 = [("milk", 20), ("bread", 15),
         ("wheat", 40), ("apple", 60)]
countcommon(list1,list2)