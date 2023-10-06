def solve(N: int, K: int) -> int:
    """
    Return the location of the K-th element in 
    an array of N-length after shuffling.
    
    N: a non-negative integer
    K: another non-negative integer
    """
    # YOUR CODE HERE
    return 0


def main():
    T = int(input())
    for _ in range(T):
        line = input().split(' ')
        N,K = int(line[0]), int(line[1])
        print(solve(N, K))

if __name__ == '__main__':
    main()
