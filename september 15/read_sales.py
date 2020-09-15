def main():
    sales_file = open('september 15/sales.txt', 'r')

    line = sales_file.readline()

    while line != '':
        amount = float(line)

        print(format(amount,'.2f'))
        line = sales_file.readline()

    sales_file.close()

main()