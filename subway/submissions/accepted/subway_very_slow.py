"""
A very very slow implementation that runs in O(N^2 * M * K^2). Used to simulate
what a beginner programmer might write. Should still pass main but not any of
the bonuses.
"""


def solve(N: int, M: int, K: int, S: list[int], E: list[int]) -> int:
    train, current_station = [], 1
    miles = 0
    while N > 0:
        for i in range(len(train)-1, -1, -1):
            if E[train[i]] == current_station:
                train.remove(train[i])
                N -= 1
        
        for i in range(len(S)):
            if S[i] == current_station and len(train) < K:
                train.append(i)
                S[i] = -1
        
        if N > 0:
            miles+= 1
        
        current_station += 1
        if current_station > M:
            current_station = 1

    return miles


def main():
    T = int(input())
    for _ in range(T):
        N, M, K = [int(x) for x in input().split()]
        S = [int(x) for x in input().split()]
        E = [int(x) for x in input().split()]
        print(solve(N, M, K, S, E))


if __name__ == '__main__':
    main()
