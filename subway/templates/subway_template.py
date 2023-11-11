def solve(N: int, M: int, K: int, S: list[int], E: list[int], P: list[int]) -> int:
    """
    Find the total distance the subway must travel until all passengers have
    arrived at their ending station.

    N: the number of passengers
    M: the number of stations
    K: the maximum number of passengers the subway can carry
    S: list of starting stations for each passenger
    E: list of ending stations for each passenger
    P: list of positions in line at their starting station for each passenger
    """
    # YOUR CODE HERE
    return -1


def main():
    T = int(input())
    for _ in range(T):
        N, M, K = [int(x) for x in input().split()]
        S = [int(x) for x in input().split()]
        E = [int(x) for x in input().split()]
        P = [int(x) for x in input().split()]
        print(solve(N, M, K, S, E, P))


if __name__ == '__main__':
    main()
