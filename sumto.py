def sumTowSmallsetNums(num):
def missingNum(listlist):
    num = sorted(num)
    sum = []
    for i in num:
        if i >= 0:
            sum.append(i)

    sumnum = sum[0] + sum[1]
    return sumnum

print(sumTowSmallsetNums([19,5,42,2,77]))
print(missingNum([1, 2, 3, 4, 6, 7, 8, 9, 10]))
print(missingNum([7, 2, 3, 6, 5, 9, 1, 4, 8]))
print(missingNum([10, 5, 1, 2, 4, 6, 8, 3, 9]))
