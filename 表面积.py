M, N = map(int, input().strip().split())
table = []
for _ in range(N):
    table.append(list(map(int, input().strip().split())))
# print(table)
def surface_area():
    area = 0
    for i in range(len(table)):
        table[i].append(0)
    table.append([0] * len(table[0]))
    for i in range(len(table) - 1):
        for j in range(len(table[0]) -1):
            if table[i][j] != 0:
                area += 2 + table[i][j] * 4 - min(table[i][j], table[i][j + 1]) *2 - min(table[i][j], table[i+1][j])*2
    print(area)
def surface():
    res = 0
    for i in range(N):
        for j in range(M):
            if table[i][j] > 0:
                res += 4 * table[i][j] + 2
                if i - 1 >=0:
                    res -= min(table[i][j], table[i-1][j])
                if i + 1 < N:
                    res -= min(table[i][j], table[i+1][j])
                if j -1 >= 0:
                    res -= min(table[i][j], table[i][j-1])
                if j+ 1< M:
                    res -= min(table[i][j], table[i][j+1])
    print(res)


# surface_area()
surface()