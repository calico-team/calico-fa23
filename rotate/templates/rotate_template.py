def solve(N: int, K: int) -> int:
    """
    Return the position of the card labelled K after shuffling a deck with N
    cards.
    
    N: the number of cards in the deck
    K: the label of the target card
    """
    # YOUR CODE HERE
    return 0


def main():
    T = int(input())
    for _ in range(T):
        line = input().split()
        N, K = int(line[0]), int(line[1])
        print(solve(N, K))

if __name__ == '__main__':
    main()
