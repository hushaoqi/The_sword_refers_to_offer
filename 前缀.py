n = int(input())
lines = []
for i in range(n):
    lines.append(input())
print(lines)
res = []
for j in range(len(lines)):  # 判断每一个字符串
    i = 0
    while i < len(lines[i]):  # 从当前字符串的首字母开始与其他字符串比较
        temp = lines[j][:i+1]  # 截取前缀

        k = 0
        while k < len(lines):
            # 检查除自身外的其他所有字符串
            if k != j and temp == lines[k][:i+1]:
                i += 1
                break
            k += 1
        if k == len(lines):
            res.append(temp)
            break
print(res)