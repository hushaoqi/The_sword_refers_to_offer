n, m = map(int, input().strip().split())
num1 = list(map(int, input().strip().split()))
num2 = list(map(int, input().strip().split()))
# print(num1, num2)
res = []
for k in range(n):
    max = -1
    n1 = -1
    n2 = -1
    for i in range(len(num1)):
        for j in range(len(num2)):
            if (num1[i] + num2[j]) % n > max:
                n1 = num1[i]
                n2 = num2[j]
                max = (num1[i] + num2[j]) % n
    num1.remove(n1)
    num2.remove(n2)
    res.append(max)
print(res)
