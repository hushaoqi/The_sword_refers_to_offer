n, m = map(int, input().split())
music = list(map(int, input().split()))
length = max(music)

while True:
    minute = 0
    i, j = 0, 1
    while j <= n:
        t = sum(music[i:j])
        if length >= t:
            j += 1
        else:  # 步长 < 和
            minute += 1
            i = j-1
            j = i + 1
    if length >= sum(music[i:n]):
        minute += 1
    if minute > m:
        length += 1
    else:
        break
print(length)
