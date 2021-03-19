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
# quick_computation = 0
# bubble_computation = 0
def quick_sort(array, qc=0):
    '''Implementation of Quick Sort Algorithm'''
    # Base Case - consider the length of the list <= 1
    # 3 arrays, 1 pivot
    left_list = []
    mid_list = [] 
    right_list = []

    qc += 1
    
    if len(array) <= 1:
        print(qc)
        return array # base case
    
    pivot = array[0] 

    for num in array:
        qc += 1
        if num < pivot:
            left_list.append(num)
        elif num == pivot: 
            mid_list.append(num)
        elif num > pivot: 
            right_list.append(num)
    return quick_sort(left_list, qc) + mid_list + quick_sort(right_list, qc)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # this is the number of loops we do
        for j in range(0, n-i-1):
            # bubble_computation += 1
            # print(bubble_computation)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Comparing the time it takes to sort a given list
quick_start_time = time.time()
print(quick_sort(sample_two))
quick_end_time = time.time()

bubble_start_time = time.time()
print(bubble_sort(sample_two))
bubble_end_time = time.time()





# Print the results
print('Quick Sort Time =>', quick_end_time - quick_start_time)
# print('Quick Sort Computations',)
print('----------------------------')
print('Bubble Sort Time =>', bubble_end_time - bubble_start_time)
# print('Bubble Sort Computations', bubble_computation)