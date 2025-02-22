

import argparse
import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def insertion_sort(a_list):
    
    start = time.time()     #Starts timing inside the sort function
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    
    end_time = time.time()
    time_bench = end_time - start
    
    return time_bench    #Returns the elapsed time

def shellSort(a_list):
    
    start = time.time()     #Starts timing inside the sort function
    sublistcount = len(a_list)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(a_list, startposition, sublistcount)
        sublistcount = sublistcount // 2
    
    end_time = time.time()
    time_bench = end_time - start
    
    return time_bench    #Returns the elapsed time

def gapInsertionSort(a_list, start, gap):
    for i in range(start+gap, len(a_list), gap):
        currentvalue = a_list[i]
        position = i
        while position >= gap and a_list[position-gap] > currentvalue:
            a_list[position] = a_list[position-gap]
            position = position - gap
        a_list[position] = currentvalue

def python_sort(a_list):
    start = time.time()     #Starts timing inside the sort function
    a_list.sort()     #Sorts the list in place
    
    end_time = time.time()
    time_bench = end_time - start
    
    return time_bench     #Returns the elapsed time

def main():
    list_sizes = [500, 1000, 5000]
    
    for the_size in list_sizes:
        for sort_function, name in [(insertion_sort, "Insertion sort"), (shellSort, "Shell sort"), (python_sort, "Python sort")]:
            total_time = 0
            for i in range(100):
                mylist = get_me_random_list(the_size)
                elapsed_time = sort_function(mylist)     #Captures the time for each sort
                total_time += elapsed_time
            avg_time = total_time / 100
            print(f"Results for list size {the_size}: {name} took {avg_time:10.7f} seconds to run, on average")

if __name__ == "__main__":
    main()





