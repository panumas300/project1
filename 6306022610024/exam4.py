pig1 = input("Enter the Pig latin word which you want to tranforms : ")

if pig1 == 'a' or pig1 == 'A':
    print(pig1+'HAY')
elif pig1 == 'e' or pig1 == 'E':
    print(pig1+'HAY')
elif pig1 == 'i' or pig1 == 'I':
    print(pig1+'HAY')
elif pig1 == 'o' or pig1 == 'O':
    print(pig1+'HAY')
elif pig1 == 'u' or pig1 == 'U':
    print(pig1+'HAY')
else :
    pig2 = pig1 + 'AY'
    
topiglatin()

frompiglatin()