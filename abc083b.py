if __name__ == '__main__':
    n, a, b = map(int, input().split())
    cnt = 0

    for i in range(1, n+1):
        target = sum(map(int, str(i)))
        if target >= a and target <= b:
            cnt += i
    ans = cnt
    print(ans)
