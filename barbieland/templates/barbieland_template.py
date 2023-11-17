def solve(N: int, M: int, Q: int, U: list[int], V: list[int], W: list[int], A: list[int], B: list[int]):
    """
    Output Q lines, where the i-th line contains the maximum
    route length possible for the i-th errand

    N: the number of dreamhouses
    M: the number of roads
    Q: the number of queries
    U: the list of U_i for each road
    V: the list of V_i for each road
    W: the list of W_i for each road
    A: the list of A_i for each query
    B: the list of B_i for each query
    """
    # YOUR CODE HERE
    return


def main():
    T = int(input())
    for _ in range(T):
        N, M, Q = [int(i) for i in input().split()]
        U, V, W = map(list, zip(*(map(int, input().split()) for _ in range(M))))
        A, B = map(list, zip(*(map(int, input().split()) for _ in range(Q))))
        solve(N, M, Q, U, V, W, A, B)


if __name__ == '__main__':
    main()
