# Apple Pi Inc.
# Algorithmic Thinking
# Fibonacci Numbers
# Iterative Approach

# iteration while loop
def fibonacci(n):
    # two initial numbers
    # in Fibonacci sequence
    a = 0
    b = 1

    i = 0
    while i < n:
        next_num = a + b
        a = b
        b = next_num
        i += 1

    return a

for i in range(10):
    print(fibonacci(i), end=" ")

        
