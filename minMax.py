def minMaxCheck(arrIn):
    minValue = arrIn[0]
    maxValue = arrIn[0]
    for eachNumber in arrIn:
        if(eachNumber < minValue):
            minValue = eachNumber
        if(eachNumber > maxValue):
            maxValue = eachNumber
    return minValue, maxValue;

n = int(input())
arrIn = []
for index in range(n):
    arrIn.append( int(input()))

minValue, maxValue = minMaxCheck(arrIn)
print(maxValue)
print(minValue)