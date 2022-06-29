def cool(n: int):
    for i in range(1, n):
        print(i * "*")
    for i in range(n, 0, -1):
        print(i * "*")


if __name__ == '__main__':
    print(cool(5))
