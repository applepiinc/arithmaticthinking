# Apple Pi Inc.
# Algorithmic Thinking
# Fibonacci Number Sequence
# Bottom Up Approach

def fib_bottomup(n):

    # fib table stores fibonacci numbers
    # initialize values to -1
    fib = []
    fib = [-1 for i in range(n)]
    
    # set the base cases
    fib[0] = 0
    fib[1] = 1

    # transition to the next state
    # repeat the process until completion
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]

    print(fib)
    return fib[n-1]

# print the 10th fib number
print("The 10th fib number is", fib_bottomup(10))



