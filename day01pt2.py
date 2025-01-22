from collections import Counter
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

columnOneCount = {i:columnOne.count(i) for i in columnOne}
columnTwoCount = {i:columnTwo.count(i) for i in columnTwo}


print(Counter(columnOne))

def countDuplicates(columnOne):
    print("Hello")