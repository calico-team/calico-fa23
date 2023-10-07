from collections import deque


def solve(N: int, K: int) -> int:
    shuffled = []
    unshuffled = deque(range(1, N + 1))
    
    while unshuffled:
        unshuffled.append(unshuffled.popleft())
        shuffled.append(unshuffled.popleft())
    
    return shuffled.index(K) + 1


def main():
    T = int(input())
    for _ in range(T):
        line = input().split()
        N, K = int(line[0]), int(line[1])
        print(solve(N, K))


if __name__ == '__main__':
    main()
