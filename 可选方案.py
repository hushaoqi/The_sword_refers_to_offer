'''
 请听题：给定N（可选作为埋伏点的建筑物数）、D（相距最远的两名特工间的距离的最大值）以及可选建筑的坐标，计算在这次行动中，大锤的小队有多少种埋伏选择。
注意：
1. 两个特工不能埋伏在同一地点
2. 三个特工是等价的：即同样的位置组合(A, B, C) 只算一种埋伏方法，不能因“特工之间互换位置”而重复使用
'''

n, dist = map(int, input().split())
nums = list(map(int, input().split()))
 
res = 0
left = 0
right = 2
 
while left < n-2:
    while right < n and nums[right] - nums[left] <= dist:
        right += 1
    if right - 1 - left >= 2:
        num = right - left - 1
        res += num * (num - 1) // 2
    left += 1
 
print(res % 99997867)
