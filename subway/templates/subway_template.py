def solve(N: int, M: int, K: int, S: list[int], E: list[int], P: list[int]) -> int:
    """
    Find the distance the subway must travel before all passengers
    arrive at their ending station

    N: the number of passengers
    M: the number of stations
    K: the capacity of the train
    S: the list of starting stations for each passenger
    E: the list of ending stations for each passenger
    P: the list of line positions for each passenger at their station
    """
    # YOUR CODE HERE
    return -1


def main():
    T = int(input())
    for _ in range(T):
        info = input().split(' ')
        N, M, K = int(info[0]), int(info[1]), int(info[2])
        S = [int(x) for x in input().split(' ')]
        E = [int(x) for x in input().split(' ')]
        P = [int(x) for x in input().split(' ')]
        solve(N, M, K, S, E, P)


if __name__ == '__main__':
    main()