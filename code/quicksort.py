from random import randint
import time

#Quick sort with pivot as last element
def quick_sort_divide(ls_elements, low_index, high_index):
    '''
    This function is used to identiy the position of pivot element in sorted list
    Inputs: unsorted list of elements, low index of given list, high index of given list
    Outputs: index of pivot element
    '''
    # assign last element in the list as pivot element
    pivot = ls_elements[high_index]
    i = low_index - 1
    for j in range(low_index, high_index):
        # if element is less than pivot then move it to left side of pivot
        if (ls_elements[j] <= pivot):
            i = i + 1
            ls_elements[i], ls_elements[j] = ls_elements[j], ls_elements[i]
    # swapping element at i+1 index with pivot
    ls_elements[i + 1], ls_elements[high_index] = ls_elements[high_index], ls_elements[i + 1]
    return i + 1


def quick_Sort(ls_elements, low_index, high_index):

    '''
    This function is used to sort the given unsorted ls_elements by using quiuck sort(pivot = last element) algorithm
    Inputs: unsorted list of elements, low index of given list, high index of given list
    Outputs: sorted list of given elements
    '''
    # if length of given list is 1 then return given list
    if len(ls_elements) == 1:
        return ls_elements
    # if low_index is less than high index then call quick_sort_divide function and get pivot index
    if low_index < high_index:
        pivot_index = quick_sort_divide(ls_elements, low_index, high_index)
        # call quick_sort function recursively for left list
        quick_Sort(ls_elements, low_index, pivot_index - 1)
        # call quick_sort function recursively for right list
        quick_Sort(ls_elements, pivot_index + 1, high_index)
    return ls_elements

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

# quick sort with pivot as last element
# store program starting time
start_ql = time.time()
sorted_list_ql = quick_Sort(unsorted_ls_elements, 0, len(unsorted_ls_elements) - 1)
# store program ending time
end_ql = time.time()
run_time_ql = end_ql - start_ql
print(
    '################################################################ Quick sort #################################################################')
print('\nThe time needed to execute Quick sort(pivot= last element) with ' + str(
    len(unsorted_ls_elements)) + ' elements is :' + str(run_time_ql) + ' seconds\n')
print('The sorted ls_elements for given elements by using quick sort(pivot = last element) technique is: ' + str(
    sorted_list_ql))
print()