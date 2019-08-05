s1, s2 = map(list, input().strip().split())
s1 = list(map(int, s1))
s2 = list(map(int, s2))

def Mul(left, right):
    Lsize = len(s1)
    Rsize = len(s2)
    size = Lsize + Rsize
    res = [0] * size
    takeover = 0  # 进位
    offset = 0  # 移位

    for idx in range(1, Rsize+1):
        takeover = 0
        rightNum = right[Rsize - idx]
        # 计算每一位与left的乘积

    return res
result = Mul(s1, s2)
print(result)