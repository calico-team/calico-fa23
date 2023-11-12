def solve(N: int, M: int, Q: int, U: list[int], V: list[int], A: list[int], B: list[int], C: list[int]):
    """
    Output Q lines, where the i-th line contains the maximum
    fuel charge possible for the i-th errand
        
    N: the number of universes
    M: the number of portals
    Q: the number of queries
    U: the list containing U_i for each query
    V: the list containing V_i for each query
    A: the list of A_i for each portal
    B: the list of B_i for each portal
    C: the list of fuel charges for each portal
    """
    # YOUR CODE HERE
    return


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        N, M, Q = int(temp[0]), int(temp[1]), int(temp[2])
        U = [None for _ in range(Q)]
        V = [None for _ in range(Q)]
        A = [None for _ in range(M)]
        B = [None for _ in range(M)]
        C = [None for _ in range(M)]
        for i in range(M):
            temp = input().split()
            A[i], B[i], C[i] = int(temp[0]), int(temp[1]), int(temp[2])
        for i in range(Q):
            temp = input().split()
            U[i], V[i] = int(temp[0]), int(temp[1])

        solve(N, M, Q, U, V, A, B, C)


if __name__ == '__main__':
    main()
