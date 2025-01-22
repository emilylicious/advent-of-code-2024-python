def readFile(fileName):
    with open(fileName, 'r') as data:
        columnOne = []
        columnTwo = []
        for line in data:
            p = line.split()
            columnOne.append(int(p[0]))
            columnTwo.append(int(p[1]))
            columnOne.sort()
            columnTwo.sort()
    return columnOne, columnTwo

columnOne, columnTwo = readFile('input.txt')
print(columnOne)
print(columnTwo)

results = [x - y for x, y in zip(columnOne, columnTwo)]
print(results)

convertPositive = (list(map(abs, results)))
print(convertPositive)

total = sum(convertPositive)
print(total)