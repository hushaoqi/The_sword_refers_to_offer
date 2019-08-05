n = int(input())
a = list(map(int, input().split()))
# print(n)
# print(a)
a = a[:n]
num = []
if n%2 == 1:
    j = n - 2
else:
    j = n - 1
i = 0
if n <= 0:
    pass
elif n == 1:
    num.append(a[0])
else:
    while i < n and j > 0:
        if a[i] < a[j]:
            num.append(a[i])
            i += 2
        else:
            num.append(a[j])
            j -= 2

    # if j <= 0 and i < n:
    #     num.append(a[n-1])
    # if i >= n and j > 0:
    #     num.append(a[1])
    if j <= 0 and i < n:
        num.extend(a[i:n:2])
    if i >= n and j > 0:
        t = a[1:j+1:2]
        num.extend(t[::-1])
for t in num:
    print(t,end=' ')