'''
输入描述:
第一行包括一个数字N，表示本次用例包括多少个待校验的字符串。
后面跟随N行，每行为一个待校验的字符串。
输出描述:
N行，每行包括一个被修复后的字符串。
示例1
输入
2
helloo
wooooooow
输出
hello
woow
'''
import sys
N = int(input())
lines = []
for k in range(N):
    try:
        lines.append(input())
    except:
        break
# print(lines[1][5])
for i in range(len(lines)):
    n = len(lines[i])
    if n < 3:pass
    if n == 3:
        if lines[i][0] == lines[i][1] == lines[2]:
            lines[i] = lines[i][:2]
        else:pass
    # 判断第一种AAA
    j = 0
    while j < len(lines[i])-2:
        if lines[i][j] == lines[i][j+1] == lines[i][j+2]:
            lines[i] = lines[i][:j]+lines[i][j+1:]
        else:
            j += 1
    # 判断第二种AABB
    j = 0
    while j < len(lines[i])-3:
        if lines[i][j] == lines[i][j+1] and lines[i][j+2] == lines[i][j+3]:
            lines[i] = lines[i][:j+2]+lines[i][j+3:]
        else:
            j += 1
for line in lines:
    print(line)


'''
n = int(input())
while n > 0:
    s = input()
    res = []
    for e in s:
        if len(res) < 2:
            res.append(e)
            continue
        if len(res) >= 2:
            if e == res[-1] and e == res[-2]:
                continue
        if len(res) >= 3:
            if e == res[-1] and res[-2] == res[-3]:
                continue
        res.append(e)
    print("".join(res))
    n -= 1
'''