if __name__ == '__main__':
    n = int(input())
    mochi = []
    for i in range(n):
        mochi.append(int(input()))

    ans = len(set(mochi))
    print(ans)
