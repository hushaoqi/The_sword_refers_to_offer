import sys
N = int(input().strip())
array = list(map(int, input().strip().split()))
fc = sys.maxsize
array.sort()
for i in range(N-2):
    nums = array[i:i+3]
    ave = sum(nums)/3
    temp = ((nums[0] - ave) ** 2 + (nums[1] - ave) ** 2 + (nums[2] - ave) ** 2)/3
    if temp < fc:
        fc = temp
print("%.2f" % fc)