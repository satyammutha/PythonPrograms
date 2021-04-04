n = int(input())
arrIn = []
for i in range(n):
    arrIn.append(int(input()))

flag = False

for j in range(n):
    if arrIn[j] > 1:
        for i in range(2, arrIn[j]):
            if (arrIn[j] % i) == 0:
                flag = True
                break
    if flag:
        print("No")
        flag = False
    else:
        print("Yes")
        flag = False