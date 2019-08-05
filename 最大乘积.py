import sys
n = int(input().strip())
array = list(map(int, input().strip().split()))
# 求出最大的三个数，和最小的两个数，选择最大三个数的和与最小两个数与最大数的和的最大值
m1, m2, m3 = -sys.maxsize, -sys.maxsize, -sys.maxsize
s1, s2 = sys.maxsize, sys.maxsize

if n < 3:
    pass
else:
    for i in range(n):

        if array[i] > m1:  # 找出最大
            m3 = m2
            m2 = m1
            m1 = array[i]
        if m2 < array[i] < m1:  # 找出第二大
            m3 = m2
            m2 = array[i]
        if m3 < array[i] < m2:  # 找出第三大
            m3 = array[i]

        if array[i] < s1:  # 找出最小
            s2 = s1
            s1 = array[i]
        if s1 < array[i] < s2:  # 找出第二小
            s2 = array[i]

    print(max(m1 * m2 * m3, m1 * s1 * s2))

# 上面的方法通不过，没找出原因
'''
n = int(input().strip())
l = list(map(int, input().strip().split()))
def max_l(l, n):
    if n < 3:
        return None
    if n == 3:
        return l[0]*l[1]*l[2]
    a, b = [], []
    a1, a2 = l[:], l[:]
    for i in range(3):
        max1 = max(a1)
        a.append(max1)
        a1.remove(max1)
    for i in range(2):
        min2 = min(a2)
        b.append(min2)
        a2.remove(min2)
    maxNum = max(a[0]*a[1]*a[2], b[0]*b[1]*a[0])
    return maxNum
print(max_l(l, n))
'''