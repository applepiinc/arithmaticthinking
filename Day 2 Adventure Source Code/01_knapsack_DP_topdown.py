# Apple Pi Inc.
# Algorithmic Thinking
# 0-1 Knapsack Problem
# DP Top Down Approach

class Item:
    def __init__(self, name: str, value: int, weight: int):
        self.name = name
        self.value = value
        self.weight = weight

# return the maximum value of given items list within weight_limit
# argument items: choices
# argument weight_limit: weight limit for each state
# recursive function
# top down approach
# return max value    
def zero_one_knapsack(items, weight_limit):

    # base cases
    if (weight_limit < 0):
        return 0

    if len(items) == 0:
        return 0
    
    # if solution in memo table
    # retrieve and use it
    if (memo[len(items)-1][weight_limit] != -1):
        return memo[len(items)-1][weight_limit]

    # otherwise, compute and
    # store the result in memo table
    max_value = -1
    
    # if current capacity < current item weight
    # then can not pick current item
    # optimal value same as the one without current item
    if (weight_limit < items[-1].weight):
        max_value = zero_one_knapsack(items[0:len(items)-1], weight_limit)
             
    else:
        # pick current item         
        value_with_current_item = \
                            zero_one_knapsack(items[0:-1], \
                            weight_limit - items[-1].weight) + \
                            items[-1].value

        # leave (do not pick) current item
        value_without_current_item = zero_one_knapsack(items[0:-1], weight_limit)

        # choose the higher value to store in dp table
        max_value = max(value_without_current_item, value_with_current_item)

    memo[len(items)-1][weight_limit] = max_value
    return max_value


# one dimension of the problem state
# weight limit
capacity = 5

# the other dimension of the problem state
# max types of items
# initialize item list and capacity
items = [Item('Water', 3, 2),
         Item('Diet Water', 1, 1),
         Item('Orange Juice', 4, 2),
         Item('Gatorade', 5, 4)]
max_items = len(items)

# initialize memo table to -1
memo = [[-1 for j in range(capacity+1)] for i in range(max_items)]  

# alternative code to initialize memo table
# memo = []
# for i in range(0, max_items):
#     line = []
#     for j in range(0, capacity+1):
#         line.append(-1)
#     memo.append(line)

# call knapsack function
max_value = zero_one_knapsack(items, capacity)

# output result
print('The maximum value within capacity:', max_value)
