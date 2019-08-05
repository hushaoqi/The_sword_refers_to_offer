n, m = map(int, input().strip().split())
flower = list(map(int, input().strip().split()))
Q = int(input().strip())
while Q > 0:
    lvalue, rvalue = map(int, input().strip().split())
    '''
    kinds = {}
    for i in range(lvalue-1, rvalue):
        if flower[i] in kinds:
            kinds[flower[i]] += 1
        else:
            kinds[flower[i]] = 1
    print(len(kinds))
    '''
    look = [0] * 101
    for i in range(lvalue-1, rvalue):
        look[flower[i]] = 1
    print(sum(look))
    Q -= 1

