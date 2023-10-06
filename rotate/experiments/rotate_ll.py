class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def solve(N, K):
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
