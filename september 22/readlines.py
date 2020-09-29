def main():
    infile = open('september 22/cities.txt', 'r')

    cities = infile.readlines()

    infile.close()

    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1

        print(cities)

main()