def sum_price(i, j, k):
    return i*500 + j*100 + k*50


if __name__ == '__main__':
    li = []
    for i in range(4):
        li.append(int(input()))

    goal_price = li[3]
    cnt = 0
    for i in range(li[0]+1):
        for j in range(li[1]+1):
            for k in range(li[2]+1):
                if sum_price(i, j, k) == goal_price:
                    cnt += 1

    ans = cnt
    print(ans)
