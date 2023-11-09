def solve(N: int, M: int, K: int, U: list[int], A: list[int], B: list[int], C: list[int]):
    """
    Output a single line containing K - 1 space-separated values denoting
    the maximum fuel charge possible for each leg of the journey.
    
    N: the number of universes
    M: the number of portals
    K: the number of errands
    U: the list containing the sequence of universes in which errands are to be completed
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
        N, M, K = int(temp[0]), int(temp[1]), int(temp[2])
        U = [int(x) for x in input().split()]
        A = [None for _ in range(M)]
        B = [None for _ in range(M)]
        C = [None for _ in range(M)]
        for i in range(M):
            temp = input().split()
            A[i], B[i], C[i] = int(temp[0]), int(temp[1]), int(temp[2])
        solve(N, M, K, U, A, B, C)

if __name__ == '__main__':
    main()
