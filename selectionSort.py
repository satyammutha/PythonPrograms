n=int(input())
arrInput = []
i = 1
for i in range(n):
    arrInput.append(int(input()))

arrInput.sort()

for x in range(n):
    print(arrInput[x])


# while(n > 0):
#     if(arrInput[n] < arrInput[n+1] ):
#         minNumber = arrInput[n]
# sortedArr.append(minNumber)
