def solve(N: int, M: int, S: list[int], E: list[int]) -> int:
    longest = 0
    for i in range(N):
        longest = max(longest, (E[i] - S[i] + M) % M)
    return longest


def main():
    T = int(input())
    for _ in range(T):
        N, M = [int(x) for x in input().split()]
        S = [int(x) for x in input().split()]
        E = [int(x) for x in input().split()]
        print(solve(N, M, S, E))


if __name__ == '__main__':
    main()
