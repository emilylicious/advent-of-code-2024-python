def totalDistance(fileName):
    with open(fileName, 'r') as data:
        columnOne = []
        columnTwo = []
        for line in data:
            p = line.split()
            columnOne.append(int(p[0]))
            columnTwo.append(int(p[1]))
            columnOne.sort()
            columnTwo.sort()
        results = [x - y for x, y in zip(columnOne, columnTwo)]
        convertPositive = (list(map(abs, results)))
        total = sum(convertPositive)
        print(total)
    return columnOne, columnTwo

columnOne, columnTwo = totalDistance('input.txt')
