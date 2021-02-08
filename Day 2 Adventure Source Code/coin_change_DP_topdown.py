# Apple Pi Inc.
# Algorithmic Thinking
# Coin Change Problem
# DP Top Down Approach

# used to get the max number
# to initialize dp table
import sys 
 
# m is size of coins array (number of 
# different coins)
def coin_change(amount):
    # base case: 0 amount needs 0 coin
    if (amount ==0):
        return 0

    # base case: negative amount has no solution
    if (amount <0):
        return -1

    # if result available in demo table, retrieve it
    if (memo[amount] != -1):
        return memo[amount]

    min = sys.maxsize
    for coin in coins:
        val = coin_change(amount-coin)
        if (val >=0 and val <min):
            min = val+1

    if min < sys.maxsize:
        memo[amount] = min
        
    return memo[amount]
 
coins = [1, 5, 6]
N = 10

# dp memo table, initialize to -1
# dp[i] stores minimum number of coins required to
# make up amount i.
memo = [-1 for i in range(N+1)]  
print("Minimum number of coins to make up $" + str(N) +
       " is", coin_change(N))
