x, y, n = map(int, input().split())
# print(x, y, n)
point = []
# boss们的坐标(0<xi<= x, 0<yi<=y)不会和小虾位置重合,用元祖列表保存
for i in range(n):
    point.append(tuple(map(int, input().split())))

def rount(a, b):
    if a == 0 and b == 0:
        return 0
    if a == 0 and b == 1 or a == 1 and b == 0:
        return 1

    elif a != 0 and b == 0:
        if (a-1, b) not in point:
            return rount(a - 1, b)
        else:
            return 0
    elif a == 0 and b != 0:
        if (a, b - 1) not in point:
            return rount(a, b - 1)
        else:
            return 0
    else:
        if (a-1, b) not in point and (a, b-1) not in point:
            return rount(a-1, b) + rount(a, b - 1)
        elif (a, b-1) not in point:
            return rount(a, b - 1)
        elif (a-1, b) not in point:
            return rount(a - 1, b)
        else:
            return 0

print(rount(x,y))