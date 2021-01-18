# Apple Pi Inc.
# Algorithmic Thinking
# 0-1 Knapsack Problem
# DP Bottom Up Approach

class Item:
    def __init__(self, name: str, value: int, weight: int):
        self.name = name
        self.value = value
        self.weight = weight

# return the maximum value of selected items within capacity
# argument items: choices
# argument capacity: knapsack capacity
def zero_one_knapsack(items, capacity):
   # dp table
   # dp[i][j] stores max value
   # for capacity j (column) considering the first i (row) items
   dp = []

   # initialize max value to 0 for all capacities and drink types
   total_item = len(items)
   for i in range (total_item+1):
      row = []
      for j in range(capacity+1):
         row.append(0)
      dp.append(row)

   # build dp table
   # from simplest problem (0 capacity, no item),
   # step by step, work towards more complicated scenarios.

   # outer for loop to gradually increase item types
   # innter for loop to gradually increase capacity
   for i in range(1, total_item+1):
      for j in range(capacity+1):
         index = i-1
         if (j < items[index].weight):
            # if current capacity < current item weight
            # then can not pick current item
            # optimal value same as the one without current item
            dp[i][j] = dp[i-1][j]
         else:
            # pick current item         
            value_with_current_item = dp[i-1][j-items[index].weight] + \
                                       items[index].value

            # leave (do not pick) current item
            value_without_current_item = dp[i-1][j]

            # choose the higher value to store in dp table
            dp[i][j] = max(value_without_current_item, value_with_current_item)

   return dp[total_item][capacity]                                                     

# initialize item list and capacity
items = [Item('Water', 3, 2),
         Item('Diet Water', 1, 1),
         Item('Orange Juice', 4, 2),
         Item('Gatorade', 5, 4)]
capacity = 5

# call knapsack function
max_value = zero_one_knapsack(items, capacity)

# output result
print('The maximum value within capacity:', max_value)
