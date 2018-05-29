if __name__ == '__main__':
    n, y = map(int, input().split())
    for i in range(0, n+1):
        for j in range(0, n+1-i):
            k = n - (i + j)
            sum_price = 10000*i + 5000*j + 1000*k
            if k >= 0 and n == i + j + k and sum_price == y:
                print(i, j, k)
                exit()
    print(-1, -1, -1)
