from collections import deque

def solve(N, K):
    unshuffled = deque(range(1, N + 1))
    shuffled = []
    while unshuffled:
        unshuffled.append(unshuffled.popleft())
        shuffled.append(unshuffled.popleft())
    return shuffled.index(K) + 1
