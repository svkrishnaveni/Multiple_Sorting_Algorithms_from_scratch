from random import randint
import time
import math

def random_list(size,lowest,highest):
    '''
    This function is used to generate random list of elements
    Inputs: size of the list, lowest element in the list, highest element in the list
    Outputs: random list of elements
    '''
    list = []
    #generating random elements
    for _ in range(size):
        value = randint(lowest, highest)
        list.append(value)
    ls_elements = list
    return ls_elements


#quick sort with pivot as median
def quick_sort_divide_median(ls_elements, low_index, high_index):
    '''
    This function is used to identiy the position of pivot element in sorted list
    Inputs: unsorted list of elements, low index of given list, high index of given list
    Outputs: index of pivot element
    '''
    median = math.floor((low_index + high_index) / 2)
    if (ls_elements[low_index] <= ls_elements[median]):
        if (ls_elements[median] <= ls_elements[high_index]):
            ls_elements[low_index], ls_elements[median] = ls_elements[median], ls_elements[low_index]
        elif (ls_elements[median] > ls_elements[high_index]):
            ls_elements[low_index], ls_elements[high_index] = ls_elements[high_index], ls_elements[low_index]
    elif (ls_elements[low_index] > ls_elements[median]):
        if (ls_elements[low_index] <= ls_elements[high_index]):
            ls_elements[low_index], ls_elements[low_index] = ls_elements[low_index], ls_elements[low_index]
        elif (ls_elements[low_index] > ls_elements[high_index]):
            ls_elements[low_index], ls_elements[high_index] = ls_elements[high_index], ls_elements[low_index]
    pivot = ls_elements[low_index]
    i = low_index
    for j in range(low_index, high_index):
        # if element is less than pivot then move it to left side of pivot
        if (ls_elements[j] < pivot):
            i = i + 1
            ls_elements[i], ls_elements[j] = ls_elements[j], ls_elements[i]
            # swapping element at i+1 index with pivot
    ls_elements[i], ls_elements[low_index] = ls_elements[low_index], ls_elements[i]
    return i


def quick_Sort_median(ls_elements, low_index, high_index):
    '''
    This function is used to sort the given unsorted ls_elements by using quiuck sort(pivot = median of 3 elements) algorithm
    Inputs: unsorted list of elements, low index of given list, high index of given list
    Outputs: sorted list of given elements
    '''
    # if length of given list is 1 then return given list
    if (len(ls_elements) == 1):
        return ls_elements
    # if low_index is less than high index then call quick_sort_divide function and get pivot index
    if (low_index < high_index):
        pivot_index = quick_sort_divide_median(ls_elements, low_index, high_index)
        # call quick_sort function recursively for left list
        quick_Sort_median(ls_elements, low_index, pivot_index)
        # call quick_sort function recursively for right list
        quick_Sort_median(ls_elements, pivot_index + 1, high_index)
    return ls_elements




# Asking input for list size
print('Enter size of the list : ')
size = int(input())

# Asking input for lowest number in the list
print('Enter Lowest number in the list : ')
lowest = int(input())

# Asking input for highest number in the list
print('Enter Highest number in the list : ')
highest = int(input())

unsorted_ls_elements = random_list(size, lowest, highest)


# quick sort with pivot as median
# store program starting time
start_qm = time.time()
sorted_list_qm = quick_Sort_median(unsorted_ls_elements, 0, len(unsorted_ls_elements) - 1)
# store program ending time
end_qm = time.time()
run_time_qm = end_qm - start_qm
print('################################################################ Quick sort(Median) #################################################################')
print('\nThe time needed to execute Quick sort(pivot = median) with ' + str(len(unsorted_ls_elements)) + ' elements is :' + str(run_time_qm) + ' seconds\n')
print('The sorted ls_elements for given elements by using quick sort(pivot = last element) technique is: ' + str(sorted_list_qm))
print()
