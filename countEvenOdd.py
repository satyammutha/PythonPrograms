n = int(input())
i = 1
arrIn = []
for i in range(n):
    arrIn.append(int(input()))

counterEven = 0
counterOdd = 0
i = 0
for i in range(n):
    if(arrIn[i] % 2 ==0):
        counterEven = counterEven + 1
    else:
        counterOdd = counterOdd + 1

print(counterOdd)
print(counterEven)