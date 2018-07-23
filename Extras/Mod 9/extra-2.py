def main():
    print("Sales Report\n")

    sales = [[1540.0, 2010.0, 2450.0, 1845.0],
             [1130.0, 1168.0, 1847.0, 1491.0],
             [1580.0, 2305.0, 2710.0, 1284.0],
             [1105.0, 4102.0, 2391.0, 1576.0]]

    head_line = "{:8} {:>12} {:>12} {:>12} {:>12}"

    counter = 0

    print(head_line.format("Region", "Q1", "Q2", "Q3", "Q4"))

    list = []
    for x in range(0,len(sales)):
        print(str(sales[0][x]) + "\t")

    """
    while True:
        for i in range(0, len(sales)):
            if i == len(sales):
                for j in range(0, len(sales)):
                    print(head_line.format(str(counter+1), str(sales[i][j]), str(sales[j][i]), str(sales[j][i]), str(sales[j][i])))
        counter += 1
        if counter == 4:
            break
    """
    

main()
