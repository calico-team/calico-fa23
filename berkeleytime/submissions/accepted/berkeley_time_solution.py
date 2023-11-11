def solve(N: int) -> str:
    if N == 0:
        return 'haha good one'
    elif N >= 180:
        return 'canceled'
    else:
        return 'berkeley' * (N // 10)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))


if __name__ == '__main__':
    main()
