# Apple Pi Inc.
# Algorithmic Thinking
# Fibonacci Numbers
# Recursive Approach

# recursive function
def fibonacci(n):
    # base case to stop the recursion call
    if (n==0):
        return 0
    if (n==1):
        return 1

    # compute fib number
    return fibonacci(n-1) + fibonacci(n-2)


# print the first 10 fib numbers
for i in range(10):
    print(fibonacci(i), end=" ")


