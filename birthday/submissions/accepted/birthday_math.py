def solve(N: int) -> int:
    return N * (N + 1) * (2 * N + 1) // 6 - N

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))

if __name__ == '__main__':
    main()
