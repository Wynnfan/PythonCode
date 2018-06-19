def printTable(tableData):
    colWidths = [0] * len(tableData)
    col = []
    for i in range(0, len(tableData[0])):
        for j in range(0, len(colWidths)):
            col.append(len(tableData[j][i]))
        max_len = max(col)

    for i in range(0, len(tableData[0])):
        for j in range(0, len(colWidths)):
            print(tableData[j][i].rjust(max_len),end='')
        print()

if __name__ == '__main__':
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    printTable(tableData)