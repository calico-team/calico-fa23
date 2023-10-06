def solve(N, K):
    deck = list(range(1, N + 1))
    for i in range(N):
        card = deck.pop(i)
        deck.append(card)
    return deck.index(K) + 1
