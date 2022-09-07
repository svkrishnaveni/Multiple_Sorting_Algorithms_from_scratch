from random import randint
import time

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

#heap sort
def heap_sort(ls_elements):
    '''
    This function is used to sort the given unsorted ls_elements by using heap sort algorithm
    Inputs: unsorted list of elements
    Outputs: sorted list of given elements
    '''
    n = len(ls_elements)
    for i in range(n, -1, -1):
        heapify(ls_elements, i, n)
    for i in range(n - 1, 0, -1):
        ls_elements[i], ls_elements[0] = ls_elements[0], ls_elements[i]
        heapify(ls_elements, 0, i)
    return ls_elements


def heapify(ls_elements, i, n):
    '''
    This function is used to heapify the given list of elements
    Inputs: list of elements, index of the root, length of the list
    Outputs: sorted list of given elements
    '''
    maxi = i
    left = 2 * i + 1
    right = 2 * i + 2
    if (left < n and ls_elements[left] > ls_elements[i]):
        maxi = left
    if (right < n and ls_elements[right] > ls_elements[maxi]):
        maxi = right
    if (maxi != i):
        ls_elements[maxi], ls_elements[i] = ls_elements[i], ls_elements[maxi]
        heapify(ls_elements, maxi, n)
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


# heap sort
# store program starting time
start_h = time.time()
sorted_list_h = heap_sort(unsorted_ls_elements)
# store program ending time
end_h = time.time()
run_time_h = end_h - start_h
print('################################################################ Heap sort #################################################################')
print('\nThe time needed to execute Heap sort with ' + str(len(unsorted_ls_elements)) + ' elements is :' + str(run_time_h) + ' seconds\n')
print('The sorted ls_elements for given elements by using heap sort technique is: ' + str(sorted_list_h))
