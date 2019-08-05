q = int(input().strip())

# 将十进制转换为k进制，k进制的每一位，用列表中的一个数表示，注意当k 大于10时，k 进制中的每一位可能为两位数
def dec2k(dec):
    ansk = []
    while dec // k:
        ansk.append(dec % k)
        dec = dec // k
    ansk.append(dec)
    ansk = ansk[::-1]
    return ansk

# 将k进制转换为十进制，k进制的每一位，用列表中的一个数表示，注意当k 大于10时，k 进制中的每一位可能为两位数
def k2dec(rans):
    ansd = 0
    tmp = 1
    for i in range(len(rans)-1, -1, -1):
        ansd += rans[i] * tmp
        tmp *= k
    return ansd
# k进制表示中，k-1的数量最多的数，且输出最小的，即k进制数每一位均为k-1构成
def get_ans():
    if len(lvalue) == 0 or len(rvalue) == 0:
        return
    # 第一种全为(k-1), l <= and <= r
    record, tmp = 0, 0
    while tmp <= r:
        record = tmp
        tmp = tmp * k + (k-1)
    # print("record:", record)
    if record >= l:
        return record

    else:
        ''' # 每判断一下都需要进制转换，复杂度太高，超时，由于每次只更新一位，因此，可以直接修改
        for i in range(len(lvalue)-1, -1, -1):
            t = lvalue[i]
            lvalue[i] = k-1
            if k2dec(lvalue) > r:  # 大于，则还原
                lvalue[i] = t
                return k2dec(lvalue)
        '''

        dec = k2dec(lvalue)
        tmp = 1
        for i in range(len(lvalue) - 1, -1, -1):
            dec = dec + (k - 1 - lvalue[i]) * tmp
            tmp = tmp * k
            t = lvalue[i]
            lvalue[i] = k - 1
            if dec > r:  # 大于，则还原
                lvalue[i] = t
                return k2dec(lvalue)

while q > 0:
    k, l, r = map(int, input().strip().split())
    lvalue = dec2k(l)  # 存放k进制的 l
    rvalue = dec2k(r)  # 存放k进制的r,数可以取的范围是[l, r]
    print(get_ans())
    q -= 1

'''
15
4 8442097414683844 8442097414683844
3 3173466882309064 3173466882309073
4 8527527027194177 8527527027194276
4 2661113491247500 2661113491248499
16 4448712248766526 4448712248776525
13 2684426398058983 2684426398158982
14 6562761408288807 6562761409288806
4 2847109288743406 2847109298743405
12 3011167199031338 3011167299031337
7 8655416323525458 8655417323525457
13 177186968879953 177196968879952
2 4133390730537405 4133490730537404
13 4680075382111731 4681075382111730
11 5341708995347620 5351708995347619
8 114951857079067 214951857079066
'''