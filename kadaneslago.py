# https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0

#code
noOfTestCases = int(input())

for x in range(noOfTestCases):
    noOfElements = int(input())
    arrayOfElements = []
    arrayOfElements = list(map(int, input().split()))
    globalMax = arrayOfElements[0]
    localMax = arrayOfElements[0]
    for y in range(1, len(arrayOfElements)):
        localMax = max(arrayOfElements[y], (localMax + arrayOfElements[y]))
        globalMax = max(localMax, globalMax)
    print(globalMax)


    
