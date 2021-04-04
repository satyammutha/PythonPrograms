def findSecondLargest(arrIn):
    largest = secLargest = 0
    for eachNumber in arrIn:
        if(largest < eachNumber):
            secLargest = largest
            largest = eachNumber
        elif(eachNumber < largest and eachNumber > secLargest):
            secLargest = eachNumber
    return secLargest;

n = int(input())
arrIn = []
for index in range(n):
    arrIn.append( int(input()))


print(findSecondLargest(arrIn))