if __name__ == '__main__':
    n = input()
    li = list(map(int, input().split(' ')))
    ans = float('inf')

    while li != []:
        li_value = li.pop()
        cnt = 0
        while li_value % 2 != 1:
            cnt += 1
            li_value /= 2
        ans = min(ans, cnt)
    print(ans)
