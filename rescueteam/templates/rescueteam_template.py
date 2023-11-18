def solve(F: int, B: int, N: int, M: int, S: int, E: int, R: list[int], U: list[int], V: list[int]):
    """
    Given the layout of a mystery dungeon, find the largest
    number of treasures you can collect before running out of belly.

    F: the number of floors in the mystery dungeon
    B: your belly value
    N: the number of rooms on each floor the of the mystery dungeon
    M: the number of hallways on each floor of the mystery dungeon
    S: the node where the starting room of each floor is located
    E: the node where the exit room of each floor is located
    R: the list of room indices where each treasure room is located
    U: the list of Ui for each hallway
    V: the list of Vi for each hallway
    """
    # YOUR CODE HERE


def main():
    T = int(input())
    for _ in range(T):
        F, B = map(int, input().split())
        N, M, S, E = map(int, input().split())
        R = [int(r) for r in input().split()]
        U, V = [None] * M, [None] * M
        for i in range(M):
            U[i], V[i] = map(int, input().split())

        print(solve(F, B, N, M, S, E, R, U, V))


if __name__ == '__main__':
    main()
