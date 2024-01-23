# Greedy
def change_greedy(coins, amount):
    # we want the minimum number of coins to make the amount
    # greedy: starting from the most coins that
    coinCount = 0
    for i in range(len(coins) - 1, -1, -1):
        if amount >= coins[i]:
            coinsUsed = amount // coins[i]
            coinCount += coinsUsed
            amount -= (coins[i] * coinsUsed)
    if amount > 0:
        return -1
    return coinCount

# BFS
# - the level is the number of coins used, this is really slow
def change_bfs(coins, amount):
    q = [0]
    level = 0
    while q:
        newQ = []
        for s in q:
            if s == amount:
                return level
            for coin in coins:
                if s + coin <= amount:
                    newQ.append(s + coin)
        q = newQ
        level += 1
    return -1

# DP
# create a list of amount, + 1, for the amount, if subtracting a coin is still within the valid range
# consider the amount a to be reachable with coin c, therefore we can minimize using what
# we already have dp[a] and 1 + dp[a - c]
# if we have no reachable coin, return -1, otherwise return the reachable
# we use amount + 1 because it is the first value less than amount, realistically this can be some
# arbitrary large number
def change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != amount + 1 else -1


coins = [1,2,5]
amount = 11
print("Input:", coins, amount)
print("Expected:", 3)
print("Received:", change(coins, amount))

coins = [2]
amount = 3
print("Input:", coins, amount)
print("Expected:", -1)
print("Received:", change(coins, amount))

coins = [1]
amount = 0
print("Input:", coins, amount)
print("Expected:", 0)
print("Received:", change(coins, amount))

coins = [1]
amount = 1
print("Input:", coins, amount)
print("Expected:", 1)
print("Received:", change(coins, amount))

coins = [1]
amount = 2
print("Input:", coins, amount)
print("Expected:", 2)
print("Received:", change(coins, amount))

# Case that doesn't work with the greey solution
coins = [1, 4, 5]
amount = 8
print("Input:", coins, amount)
print("Expecte:", 2)
print("Received:", change(coins, amount))