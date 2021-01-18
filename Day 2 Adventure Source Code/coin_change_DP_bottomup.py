# Apple Pi Inc.
# Algorithmic Thinking
# Coin Change Problem
# DP Bottom Up Approach

# used to get the max number
# to initialize dp table
import sys 
 
# m is size of coins array (number of 
# different coins)
def coin_change(amount):
    # dp table
    # dp[i] stores minimum number of coins required to
    # make up amount i.
    dp = []

    # set initial values to infinite 1..N table cells
    for i in range(N+1):
        dp.append(sys.maxsize)

    # alternative code  
    # dp = [sys.maxsize for i in range(N + 1)]    

    # base case: 0 amount needs 0 coin
    dp[0] = 0

    # build dp table
    # from simplest problem (0 amount),
    # step by step, work towards N.
    for i in range(1, N + 1):
         
        # Go through all coins smaller than i
        for coin in coins:
            if (coin <= i):
                previous_result = dp[i - coin]
                #if (previous_result != sys.maxsize and
                #    previous_result + 1 < dp[i]):
                if (previous_result + 1 < dp[i]):
                    dp[i] = previous_result + 1
    return dp[N]
 
coins = [1, 5, 6]
N = 10
print("Minimum number of coins to make up $10 is ", 
                 coin_change(N))
