def solve(N: int, K: int) -> int:
    if K % 2 == 0:
        return K // 2
    
    if N % 2 == 0:
        return N // 2 + solve(N // 2, K // 2 + 1)
    else:
        if K == 1:
            return N // 2 + 1
        return N // 2 + 1 + solve(N // 2, K // 2)


def main():
    T = int(input())
    for _ in range(T):
        line = input().split()
        N, K = int(line[0]), int(line[1])
        print(solve(N, K))


if __name__ == '__main__':
    main()
