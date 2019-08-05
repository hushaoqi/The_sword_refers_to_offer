def gcd(m, n):
    if(m % n == 0):
        return n

    return gcd(n, m % n)

if __name__=='__main__':
    n = input()
    # a = list(map(int, input().strip().split()))
    a = list(map(int, input().split(' ')))
    for i in range(0, int(n)):

        if i == 0:
            x = a[i]

        else:
            x = gcd(x, a[i])
    print(x)
    count = 0
    for i in range(int(n)):
        count += a[i]//x
    print(count)
