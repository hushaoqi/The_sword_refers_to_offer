string = input().strip()
table = [0] * 52
low = ''
up = ''
for s in string:
    if ord('A') <= ord(s) <= ord('Z'):
        if table[ord(s) - ord('A')] == 0:
            # up += s
            table[ord(s) - ord('A')] += 1
        else:
            table[ord(s) - ord('A')] += 1
    else:
        if table[ord(s) - ord('a') + 26] == 0:
            # low += s
            table[ord(s) - ord('a') + 26] += 1
        else:
            table[ord(s) - ord('a') + 26] += 1
print(table)
flag = False
for s in string:
    if (ord('A') <= ord(s) <= ord('Z') and table[ord(s) - ord('A')] == 1) or ((ord('a') <= ord(s) <= ord('z') and table[ord(s) - ord('a')+26] == 1)):
        flag = True
    if table[ord(s) - ord('A')] != 0 and (0 <= ord(s) - ord('A') <= 25) and flag is True:
        up += chr(ord('A')+ ord(s) - ord('A'))
        table[ord(s) - ord('A')] = 0
    if table[ord(s) - ord('a')+26] != 0 and (26 <= ord(s) - ord('a')+26 <= 51) and flag is True:
        low += chr(ord('a') + ord(s) - ord('a'))
        table[ord(s) - ord('a') + 26] = 0
print(table)
res = up + low
print(res)

