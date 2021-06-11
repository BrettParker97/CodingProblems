import itertools

def makeChange(coins, n):
    for x in range(1, len(coins)):
        temp = itertools.combinations(coins, x)
        for y in temp:
            temp2 = sum(y)
            if temp2 == n:
                return y
    return None
    
print(makeChange({1, 5, 25, 10}, 36))