def removee(mylist):
    mylist = list(dict.fromkeys(mylist))
    return mylist

print(removee(['The','b','The']))
print(removee(['1','0','1','0']))
print(removee(['a','b','a','b','c']))
print(removee([1,2,1]))