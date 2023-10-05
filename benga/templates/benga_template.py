def solve(N: int) -> int:
    """
    Return the number of possible towers that Big Ben can build with N blocks.
    
    N : number of 1x1x3 Benga Bricks we can use to construct the Benga tower.
    """
    # YOUR CODE HERE
    return 0


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))

if __name__ == '__main__':
    main()
