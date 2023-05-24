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
        info = input().strip().split(' ')
        F, B = int(info[0]), int(info[1])

        info = input().strip().split(' ')
        N, M, S, E = int(info[0]), int(info[1]), int(info[2]), int(info[3])

        X = [None for _ in range(M)]
        Y = [None for _ in range(M)]
        U = [None for _ in range(F)]
        V = [None for _ in range(F)]

        for i in range(M):
            info = input().strip().split(' ')
            X[i], Y[i] = int(info[0]), int(info[1])
        
        for i in range(F):
            info = input().strip().split(' ')
            U[i], V[i] = int(info[0]), int(info[1])
        
        solve(F, B, N, M, S, E, X, Y, U, V);

if __name__ == '__main__':
    main()