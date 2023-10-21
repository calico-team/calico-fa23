def solve(A: int) -> str:
    """
    Return the berkeleytime value of A.
    
    A: a non-negative integer
    """
    solutionString = "berkeley"
    if A > 180:
        return "canceled"
    solutionString = solutionString * (A % 10)
    return solutionString + "time"


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        A = int(temp[0])
        print(solve(A))

if __name__ == '__main__':
    main()
