def solve(A: int) -> int:
    """
    TODO: 
    
    A: a non-negative integer
    """
    # YOUR CODE HERE
    numDays =0
    for year in range(1,A + 1):
        numDays += year**2
    return numDays +3


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        A = int(temp[0])
        print(solve(A))

if __name__ == '__main__':
    main()
