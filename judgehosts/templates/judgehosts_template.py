def solve(N: int, M: int, S: int, U: list[int], V: list[int]):
    """
    Output any list of x <= S computers Bessie can eat such that the network is not bridged afterwards.
    If it's impossible, output IMPOSSIBLE
    
    N: Number of computers.
    M: Number of connections between computers.
    S: Number of computers Bessie can eat.
    U: Initial computer for each of the M connections.
    V: Final computer for each of the M connections.
    """
    # YOUR CODE HERE
    return

def main():
    T = int(input())
    for _ in range(T):
        info = input().strip().split(' ')
        N, M, S = int(info[0]), int(info[1]), int(info[2])
        U, V = [], []
        for i in range(M):
            info = input().strip().split(' ')
            U.append(int(info[0]))
            V.append(int(info[1]))
        solve(N, M, S, U, V)

if __name__ == '__main__':
    main()