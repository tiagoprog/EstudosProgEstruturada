while True:
    N = int(input())
    if N == 0:
        break
    
    results = list(map(int, input().split()))
    mary_wins = results.count(0)
    john_wins = results.count(1)
    
    print("Mary won", mary_wins, "times and John won", john_wins, "times")