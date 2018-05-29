if __name__ == '__main__':
    n = int(input())
    cardlist = list(map(int, input().split()))
    cardlist.sort()

    alice_s, bob_s = 0, 0
    while cardlist != []:
        alice_s += cardlist.pop()
        if cardlist == []:
            break
        bob_s += cardlist.pop()
    ans = alice_s - bob_s
    print(ans)
