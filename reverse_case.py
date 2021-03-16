def reverse_case(txt):
    x=''
    for item in txt:
        if item.isupper()==True:
            x+=item.lower()
        else:
            x+=item.upper()
    return x

print(reverse_case("Spiderman"))
print(reverse_case("SPIDER "))
