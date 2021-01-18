# Apple Pi Inc.
# Algorithmic Thinking
# Fractional Knapsack Problem
# Greedy Approach

class Item:
    def __init__(self, name: str, value: int, weight: int):
        self.name = name
        self.value = value
        self.weight = weight

# return (max_value, fractions)
#   max_value: the maximum value of selected items within capacity
#   fractions: dictionary showing selected items and the serving fractions (0,1]
# argument items: choices
# argument capacity: knapsack capacity
def fractional_knapsack(items, capacity):
 
    # reverse sort the items by value/weight ratio (high ratio on top)
    # lambda represent a small function without name (called anonymous function)
    # format 'lambda arguments: expression'
    # here, the argument is each item in the items list
    # the expression is the ratio
    # use this lambda function to sort items by ratio in reverse order
    items.sort(key=lambda item: item.value/item.weight, reverse=True)

    max_value = 0
    fractional_amt = {}

    # Greedy approach to take high value/weight ratio items by order
    for item in items:
        
        if item.weight <= capacity:
            # include the whole serving
            fractional_amt[item] = 1
            max_value += item.value
            capacity -= item.weight
        else:
            # include partial serving
            fraction_to_add = capacity/item.weight
            fractional_amt[item] = fraction_to_add
            max_value += item.value * fraction_to_add
            break

    return max_value, fractional_amt

# initialize item list and capacity
items = [Item('Honey Roasted Peanuts', 90, 30),
         Item('Salted Sunflower Seed', 45, 30),
         Item('Coconut Water', 140, 80),
         Item('Chocolate Hawaii Macadamia Nuts', 90, 20)]
capacity = 100

# call knapsack function
max_value, fractions = fractional_knapsack(items, capacity)

# output result
print('The maximum value of items that can be taken within capacity:', max_value)
for item in fractions:
    print("item: " + str(item.name) + ', ', end='')
    print("amount: " + str(fractions[item]))
