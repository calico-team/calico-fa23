import collections


def dfs(S, index, A, B):
    counter = collections.Counter(S)
    for a in A:
        for b in B:
            counter[a + b] -= 1
            if counter[a + b] < 0:
                return False

    if len(A) == 6 and len(B) == 6:
        return A, B

    for c in counter:
        if counter[c] != 0:
            break

    if len(A) < 6:
        result = dfs(S, index + 1, [*A, c], B)
        if result:
            return result

    if len(B) < 6:
        result = dfs(S, index + 1, A, [*B, c])
        if result:
            return result

    return False


def solve(S: list[int]):
    S = [i - 2 for i in S]
    S0 = S[0]
    S = [i - S0 for i in S]

    result = dfs(S, 2, [0, S[1]], [0])
    if not result:
        print("IMPOSSIBLE")
        return

    A, B = result
    print(' '.join(map(str, [a + 1 + S0 for a in A])))
    print(' '.join(map(str, [b + 1 for b in B])))


def main():
    T = int(input())
    for _ in range(T):
        S = [int(x) for x in input().split()]
        solve(S)


if __name__ == '__main__':
    main()
