def solve(N: int) -> int:
    ans = 0
    for i in range(1, N // 3 + 1) :
        ans = ans + pow(2, i, 3359232)
        ans = ans % 3359232
    return ans


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))


if __name__ == '__main__':
    main()