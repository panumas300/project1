def missingNum(listlist):

    emptylist = []
    testlist = [1,2,3,4,5,6,7,8,9,10]
    for i in listlist:
        if i == 1:
            emptylist.append(i)
        elif i == 2:
            emptylist.append(i)
        elif i == 3:
            emptylist.append(i)
        elif i == 4:
            emptylist.append(i)
        elif i == 5:
            emptylist.append(i)
        elif i == 6:
            emptylist.append(i)
        elif i == 7:
            emptylist.append(i)
        elif i == 8:
            emptylist.append(i)
        elif i == 9:
            emptylist.append(i)
        elif i == 10:
            emptylist.append(i)



    for i in testlist:
        if i == emptylist:
            testlist.pop(i)

    return testlist


print(missingNum([1, 2, 3, 4, 6, 7, 8, 9, 10]))
print(missingNum([7, 2, 3, 6, 5, 9, 1, 4, 8]))
print(missingNum([10, 5, 1, 2, 4, 6, 8, 3, 9]))

'''
def removee(mylist):
    mylist = list(dict.fromkeys(mylist))
    return mylist

print(removee(['The','b','The']))
print(removee(['1','0','1','0']))
print(removee(['a','b','a','b','c']))
print(removee([1,2,1]))
'''