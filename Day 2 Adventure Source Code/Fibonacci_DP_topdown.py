# Apple Pi Inc.
# Algorithmic Thinking
# Fibonacci Number Sequence
# DP Top Down Approach With Recursive Function

fib = [-1 for i in range(10)]
def fib_topdown(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1

    # if result available in memo table, retrieve it
    if(fib[n] != -1):
        return fib[n]

    # store result in memo table
    fib[n] = fib_topdown(n - 1) + fib_topdown(n - 2);
    return fib[n];

# print the 10th fib number (on index 9)
print("The 10th fib number is", fib_topdown(9))

