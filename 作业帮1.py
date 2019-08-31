x, n = map(int, input().strip().split())
n += 1
res = 0
if x == 1:
    res = n % 998244353 - 1
else:
    res = (1-x ** n) / (1-x) % 998244353 - 1
print(int(res))
