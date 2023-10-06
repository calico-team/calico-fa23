def solve(N: int, K: int) -> int:
    """
    Return the position of the card labelled K after shuffling a deck with N
    cards.
    
    N: the number of cards in the deck
    K: the label of the target card
    """
    # YOUR CODE HERE
    if N % 2 == 0:
        if K % 2 == 0:
            return K // 2
        return N // 2 + solve(N // 2, K // 2 + 1)
    else:
        if K % 2 == 0:
            return K // 2
        if K == 1:
            return N // 2 + 1
        return N // 2 + 1 + solve(N // 2, K // 2)



def main():
    T = int(input())
    for _ in range(T):
        line = input().split()
        N, K = int(line[0]), int(line[1])
        print(solve(N, K))

if __name__ == '__main__':
    main()
