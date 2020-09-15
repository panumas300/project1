def main():
    infile = open('september 15/philosophers.txt','r')

    file_contents = infile.read()

    infile.close()

    print(file_contents)

main()