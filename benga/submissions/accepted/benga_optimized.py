# TODO finish implementing

A = [
    [2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
]

def solve(N: int) -> int:
    """
    TODO write problem summary
    
    N: the height of the tower
    """
    # YOUR CODE HERE
    return 0


def matpow(A, A_dim, n, mod):
    A_rows, A_cols = A_dim
    
    curr_power = A.copy()
    result = [1 if i == j else 0 for i in range(A_rows) for j in range(A_cols)]
    if n & 1:
        result = A.copy()
    n >>= 1
    
    while n:
        curr_power = matmul(curr_power, A_dim, curr_power, A_dim, mod)
        if n & 1:
            result = matmul(curr_power, A_dim, result, A_dim, mod)
        n >>= 1
    return result


def matmul(A, A_dim, B, B_dim, mod):
    A_rows, A_cols = A_dim
    B_rows, B_cols = B_dim
    AB_rows, AB_cols = A_rows, B_cols
    
    return [
        sum(
            A[A_cols * i + k] * B[B_cols * k + j]
            for k in range(A_cols)
        ) % mod
        for i in range(AB_rows)
        for j in range(AB_cols)
    ]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))

if __name__ == '__main__':
    main()
