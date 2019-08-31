L, N = map(int, input().strip().split())
location = list(map(int, input().strip().split()))
location.sort()
maxabs = 0
for i in range(N-1):
    if maxabs < location[i+1] - location[i]:
        left = location[i]
        right = location[i+1]
        maxabs = location[i+1] - location[i]
if maxabs < (location[0] + L - location[-1]):
    left = location[0]
    right = location[-1]
    maxabs = location[0] + L - location[-1]
print(left, right, maxabs)
mid = left + right  # 中心点
res = 0
if maxabs in location:
    temp = 0
else:
    temp = 1
for num in location:
    if num <= left:
        res += (num + L) - mid - temp
        temp += 1
temp = 0
location = location[::-1]
for num in location:
    if num >= right:
        res += mid - num - temp
        temp += 1
print("res",  res)


'''
1000 4
1 4 995 998
'''
