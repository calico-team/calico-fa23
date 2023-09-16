def solve(A: int) -> int:
    """
    TODO: 
    
    A: a non-negative integer
    """
    # YOUR CODE HERE
    return A*(A-1)*(2*A-1) // 6 +3


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        A = int(temp[0])
        print(solve(A))

if __name__ == '__main__':
    main()
