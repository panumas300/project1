def main():
    cities = ['New York','Boston','Atlanta','Dallas']

    outfile = open('september 22/cities.txt','w')
    outfile.writelines(cities)
    outfile.close()

main()