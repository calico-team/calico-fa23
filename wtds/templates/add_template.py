def solve() -> None:
    """
    Find the unknown datamon through feed, poop, and guess queries.
    
    Call the feed, poop, and guess functions below to make feed, poop, and guess queries.
    """
    # YOUR CODE HERE

"""
    Feed the datamon an integer
"""
def feed(i: int) -> str:
    print("feed", i, flush = True)
    response = input()
    if response == "WRONG_ANSWER":
        exit()
    return response

"""
    Datamon poops out an integer depending on its species 
"""
def poop() -> int:
    print("poop", flush = True)
    response = input()
    if response == "WRONG_ANSWER":
        exit()
    return int(response)

"""
    Guess the datamon 
"""
def guess(i: str) -> str:
    print("guess", i, flush = True)
    response = input()
    if response == "WRONG_ANSWER":
        exit()
    return int(response)

def main():
    T = int(input())
    for _ in range(T):
        solve()
    verdict = input()


if __name__ == '__main__':
    main()