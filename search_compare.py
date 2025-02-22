#!/usr/bin/env python
# coding: utf-8

# In[235]:


import time
import random


# In[249]:


def get_me_random_list(n):
    
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    start = time.time()   #Starts timing inside the function before search begins
    
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    
    end_time = time.time()
    time_bench = end_time - start
    
    return found, time_bench


def ordered_sequential_search(a_list, item): 
    start = time.time()   #Starts timing inside the function before search begins
    
    pos = 0
    found = False
    stop = False
    
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    
    end_time = time.time()
    time_bench = end_time - start
    
    return found, time_bench


def binary_search_iterative(a_list,item):
    start = time.time()    #Starts timing inside the function before search begins
    
    first = 0
    last = len(a_list) - 1
    found = False
    
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    
    end_time = time.time()
    time_bench = end_time - start
    
    return found, time_bench


def binary_search_recursive(a_list, item):
    start = time.time()     #Starts timing inside the function before search begins

    def search(a_list, item):
        if len(a_list) == 0:
            return False
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            return search(a_list[:midpoint], item)
        else:
            return search(a_list[midpoint + 1:], item)

  
    found = search(a_list, item)
    end_time = time.time()
    time_bench = end_time - start 

    return found, time_bench 


def benchmark_test(listicle_size):
    
    total_time_sequential = 0
    total_time_ordered_sequential = 0
    total_time_binary_iterative = 0
    total_time_binary_recursive = 0
    
    for i in range(100):
        my_list = get_me_random_list(listicle_size)
        
        
        #Sequential search
        result, time_taken = sequential_search(my_list, 99999999)
        total_time_sequential += time_taken

        #Ordered Sequential search
        my_list_sorted = sorted(my_list)
        result, time_taken = ordered_sequential_search(my_list_sorted, 99999999)
        total_time_ordered_sequential += time_taken

        #Binary Search Iterative
        result, time_taken = binary_search_iterative(my_list_sorted, 99999999)
        total_time_binary_iterative += time_taken

        #Binary Search Recursive
        result, time_taken = binary_search_recursive(my_list_sorted, 99999999)
        total_time_binary_recursive += time_taken
        
    
    #Finding avg time to complete
    avg_time_sequential = total_time_sequential / 100
    avg_time_ordered_sequential = total_time_ordered_sequential / 100
    avg_time_binary_iterative = total_time_binary_iterative / 100
    avg_time_binary_recursive = total_time_binary_recursive / 100
    
    print(f"Results for list size {listicle_size}: Sequential Search took {avg_time_sequential:10.7f} seconds to run, on average")
    print(f"Results for list size {listicle_size}: Ordered Sequential Search took {avg_time_ordered_sequential:10.7f} seconds to run, on average")
    print(f"Results for list size {listicle_size}: Binary Iterative Search took {avg_time_binary_iterative:10.7f} seconds to run, on average")
    print(f"Results for list size {listicle_size}: Binary Recursive Search took {avg_time_binary_recursive:10.7f} seconds to run, on average\n")
    
    
def main():
    for size in [500, 1000, 5000]:
        benchmark_test(size)    
  

if __name__ == "__main__":
    main()

