def solve(N, K):
    if N % 2 == 0:
        if K % 2 == 0:
            return K // 2
        return N // 2 + solve(N // 2, K // 2 + 1)
    else:
        if K % 2 == 0:
            return K // 2
        if K == 1:
            return N // 2 + 1
        return N // 2 + 1 + solve(N // 2, K // 2)
