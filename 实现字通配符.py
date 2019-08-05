T = input()
S = input()
# print(T, S)
Tlen = len(T)
Slen = len(S)
i, j = 0
while i < Tlen and j < Slen:
    if T[i] == '*':
        