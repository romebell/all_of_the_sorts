# All of the Sorts

```py
# Implementing Quick Sort
# Explain the code line by line
# Test the code
# Track the time it takes to run that algorithm
# Compare the quick_sort time with bubble_sort time

# Bubble Sort -> O(n^2) 
# Quick Sort -> O(log(n)) miles faster than Bubble Sort

import random, time

sample_one = random.sample(range(1, 1000000), 100)
sample_two = random.sample(range(1, 1000000), 9999)
sample_three = random.sample(range(1, 1000000), 200000)

def quick_sort(array):
    '''Implementation of Quick Sort Algorithm'''
    # Base Case - consider the length of the list <= 1
    # 3 arrays, 1 pivot
    left_list = [] # [1]
    mid_list = [] # [20]
    right_list = [] # [22]

    
    if len(array) <= 1:
        return array # base case
    
    pivot = array[0] # 20

    for num in array:
        if num < pivot: 
            left_list.append(num)
        elif num == pivot: 
            mid_list.append(num)
        elif num > pivot: 
            right_list.append(num)
    
    return quick_sort(left_list) + mid_list + quick_sort(right_list)

num_list = [88, 32, 77, 20, 1, 22]

quick_sort(num_list)

# 1.0 run
# left_list = [] # [32, 77, 20, 1, 22] -> result of 2.0
# mid_list = [] # [88]
# right_list = []

# finished: [1, 20, 22, 32, 77, 88]

# 2.0 run (left side)
# left_list = [20, 1, 22] -> solve 2.1
# mid_list = [32] 
# right_list = [77] ???

# finish [1, 20, 22] + [32] + [77] = [1, 20, 22, 32, 77]

# 2.1 ()
# [1, 20, 22]
```
