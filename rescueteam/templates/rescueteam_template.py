def solve(F: int, B: int, N: int, M: int, S: int, E: int, X: list[int], Y: list[int], U: list[int], V: list[int]):
    '''
    Given the layout of a mystery dungeon, find the largest
    value of treasure you can collect before running out of belly.
    
    F: the number of floors in the mystery dungeon
    B: your belly capacity
    N: the number of nodes on each floor the of the mystery dungeon
    M: the number of edges on each floor of the mystery dungeon
    S: the node where the spawn point is located
    E: the node where the exit stairwell is located
    X: the list of X_i for each undirected edge
    Y: the list of Y_i for each undirected edge
    U: the node where the treasure on floor i is located
    V: the value of the treasure on floor i
    '''
    # YOUR CODE HERE


def main():
    T = int(input())
    for _ in range(T):
        F, B = map(int, input().split())
        N, M, S, E = map(int, input().split())

        X, Y = [None] * M, [None] * M
        for i in range(M):
            X[i], Y[i] = map(int, input().split())

        U, V = [None] * F, [None] * F
        for i in range(F):
            U[i], V[i] = map(int, input().split())
        
        print(solve(F, B, N, M, S, E, X, Y, U, V))


if __name__ == '__main__':
    main()
