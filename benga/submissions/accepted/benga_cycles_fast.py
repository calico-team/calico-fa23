"""
Same as benga_cycles.py but with some constant factor optimizations.
"""


import sys


sys.set_int_max_str_digits(10 ** 6)

"""Precomputed Augmented Border State Transition Matrix

See benga/experiments/misc/make_matrix.py for an explanation.
"""
A_1 = [
    2, 0, 4, 0, 0, 0, 2, 0, 4, 0, 0, 0, 0, 0, 0, 2, 0, 1, 1,
    1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
    1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
    0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
]
dim_A = 19

I = [int(i == j) for i in range(dim_A) for j in range(dim_A)]
A = [I, A_1]

MOD = 2 ** (3 ** 2) * 3 ** (2 ** 3)

"""Precomputed Matrix Power Cycle Length

See benga/submissions/accepted/benga_cycles.cpp for an explanation.
"""
LAMBDA = 84 * 312 * 6 * MOD


def solve(N: int) -> int:
    A_N = mat_pow_mod(A, N // 3 % LAMBDA)
    return (A_N[19 - 1] + A_N[0] - 1) % MOD


def mat_pow_mod(A, n):
    result = I.copy()
    bin_n = bin(n)
    for i in range(1, len(bin_n) - 1):
        if bin_n[-i] == '1':
            result = mat_mul_mod(A[i], result)
        if len(A) < i + 2:
            A.append(mat_mul_mod(A[-1], A[-1]))
    return result


def mat_mul_mod(A, B):
    return [
        sum(
            A[dim_A * i + k] * B[dim_A * k + j]
            for k in range(dim_A)
        ) % MOD
        for i in range(dim_A)
        for j in range(dim_A)
    ]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))


if __name__ == '__main__':
    main()
