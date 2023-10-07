class LinkedListNode:
        def __init__(self, val):
            self.val = val
            self.next = None
         
def solve(N: int, K: int) -> int:
    """
    Return the position of the card labelled K after shuffling a deck with N
    cards.
    
    N: the number of cards in the deck
    K: the label of the target card
    """
    # YOUR CODE HERE     
    sentinel = curr = top = LinkedListNode(None)
    for i in range(1, N + 1):
        top.next = LinkedListNode(i)
        top = top.next
    for _ in range(N):
        top.next = curr.next
        curr.next = curr.next.next
        top = top.next
        curr = curr.next
    for i in range(1, N + 1):
        sentinel = sentinel.next
        if sentinel.val == K:
            return i


def main():
    T = int(input())
    for _ in range(T):
        line = input().split()
        N, K = int(line[0]), int(line[1])
        print(solve(N, K))

if __name__ == '__main__':
    main()
