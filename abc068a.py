if __name__ == '__main__':
    a, b = map(int, input().split(' '))
    a, b = map(int, input().split(' '))
    ans = a * b
    if ans % 2 == 0:
        print('Even')
    else:
        print('Odd')
