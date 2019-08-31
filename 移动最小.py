L, N = map(int, input().strip().split())
location = list(map(int, input().strip().split()))
location.sort()
maxabs = 0
space = []
for i in range(N-1):
    c = location[i + 1] - location[i]
    space.append(c)
    if maxabs < c:
        left = location[i]
        right = location[i+1]
        maxabs = c

c = location[0] + L - location[-1]
space.append(c)
if maxabs < c:
    left = location[0]
    right = location[-1]
    maxabs = c
print(left, right, maxabs)
if maxabs in location:
    print(sum(space) - maxabs - 2)
else:
    print(sum(space) - maxabs - 1)

'''
1000 4
1 4 995 998


'''