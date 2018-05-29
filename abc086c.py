if __name__ == '__main__':
    n = int(input())
    tl, xl, yl = [], [], []
    for i in range(n):
        t, x, y = map(int, input().split())
        tl.append(t)
        xl.append(x)
        yl.append(y)

    prex, prey, pret = 0, 0, 0
    for t, x, y in zip(tl, xl, yl):
        sumxy = x + y - prex - prey
        sumt = t - pret
        prex, prey, pret = x, y, t
        if sumxy > sumt or sumt % 2 != sumxy % 2:
            print('No')
            exit()
    print('Yes')
